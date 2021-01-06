#!/usr/bin/env python3
import boto3
from datetime import timedelta, datetime
from botocore.exceptions import ClientError
import requests
from multiprocessing import Process, Pipe
import urllib3
urllib3.disable_warnings()

'''
   - Lekgalwa Ngoatje - 2020/09/13
'''
cloud_watch_client = dict()
zar_rate = 0



def lambda_handler(event, context):
    global cloud_watch_client
    try:
        total_sum = 0
        # Security Credential
        total = total_consumption_all_attachments()
        for n, item in enumerate(total):
            total_sum += item["bytes_processed"]
            print("sum for :", str(n) + " : " + str(item["attachment_id"]) + " => " + str(
                item["bytes_processed"]))
        print("total results: => ", str(total_sum))
    except ClientError as e:
        # Send some context about this error to Lambda Logs
        print("Error executing Lambda in SCP Test Engineering AWS account.", e)
    else:
        print("\nLambda executed successfully")
    finally:
        print('\nDone! ' + datetime.now().strftime("%Y/%m/%d %H:%M:%S") + '\n')


def get_tgw_metric_list(cred_cross_account_role):
    client = boto3_service('cloudwatch', cred_cross_account_role)
    dimensions_list = []
    response = client.list_metrics(
        Namespace = "AWS/TransitGateway",
        MetricName = "BytesIn",
        Dimensions = [
            {
                "Name": "TransitGateway",
                "Value": "tgw-0287771349e8cb90e"
            }
        ]
    )
    for metric_item in response["Metrics"]:
        for dimension in metric_item["Dimensions"]:
            if dimension["Name"] == "TransitGatewayAttachment":
                dimensions_list.append(str(dimension["Value"]))
    return dimensions_list

def added_costs():
    # TODO: get cost from cost explorer
    tgw_vpc_attachment_hour = 0.05
    tgw_vpn_attachment_hour = 0.05


def get_list_of_gateway_attachments(cred_cross_account_role: dict):
    attachment_ids = []
    client = boto3_service('ec2', cred_cross_account_role)
    paginator = client.get_paginator('describe_transit_gateway_attachments')
    response_iterator = paginator.paginate()
    for page in response_iterator:
        for json_data in page['TransitGatewayAttachments']:
            attachment_ids.append(json_data.get("TransitGatewayAttachmentId"))
    return attachment_ids


def get_daily_attachment_data(dates: dict, transit_gateway_attachment: str, conn):

    sum_data = 0
    # specify start and end dates
    for current_day in dates:
        next_day = current_day + timedelta(days = 1)

        cw_bytes_in_response = get_tgw_metrics("BytesIn", current_day, next_day, str(transit_gateway_attachment))

        if len(cw_bytes_in_response.get("Datapoints")):
            stats_data = cw_bytes_in_response.get("Datapoints")[0]
            sum_data += stats_data.get("Sum")

    model = attachment_model(transit_gateway_attachment, dates[0], dates[-1], sum_data)
    conn.send([model])
    conn.close()


def get_tgw_metrics(metric_name: str, current_day: datetime, next_day: datetime, transit_gateway_attachment_id: str):
    global cloud_watch_client
    return cloud_watch_client.get_metric_statistics(
        Namespace = "AWS/TransitGateway",
        MetricName = metric_name,
        Dimensions = [
            {
                "Name": "TransitGateway",
                "Value": "tgw-0287771349e8cb90e"
            },
            {
                "Name": "TransitGatewayAttachment",
                "Value": transit_gateway_attachment_id
            }
        ],
        StartTime = current_day,
        EndTime = next_day,
        Period = 3600 * 24 * 1,
        Statistics = [
            "Sum"
        ]
    )


def get_monthly_date_list():
    start_date, end_date = get_previous_month_start_end_date()
    return create_date_list(start_date, end_date)


def total_consumption_all_attachments():
    global cloud_watch_client
    global zar_rate

    cred_cross_account_role = sts_assume_cross_account_role()
    cloud_watch_client = boto3_service("cloudwatch", cred_cross_account_role)
    tgw_attachments_list = get_tgw_metric_list(cred_cross_account_role)

    tgw_attachments_group_model_results = []
    dates = get_monthly_date_list()

    # zar rate
    zar_rate = fetch_latest_conversion_rate_data()

    print("Running in parallel")

    # create a list to keep all processes
    processes = []

    # create a list to keep connections
    parent_connections = []

    # iterate through list for transit-gateway flow-log daily data extraction
    # create a process per attachment
    for attachment_dict in tgw_attachments_list:
        # create a pipe for communication
        parent_conn, child_conn1 = Pipe()
        parent_connections.append(parent_conn)

        # create the process, pass instance and connection
        bytes_process = Process(target = get_daily_attachment_data, args = (dates, attachment_dict, child_conn1,))
        processes.append(bytes_process)


    # start all processes
    for process in processes:
        process.start()

    # make sure that all processes have finished
    for process in processes:
        process.join()

    for parent_connection in parent_connections:
        tgw_attachments_group_model_results.append(parent_connection.recv()[0])


    return tgw_attachments_group_model_results


def attachment_model(attachment, date_start, date_end, bytes_processed):
    global zar_rate
    attachment_dict = dict()
    attachment_dict['attachment_id'] = attachment
    attachment_dict['date_start'] = date_start
    attachment_dict['date_end'] = date_end
    attachment_dict['bytes_processed'] = bytes_processed
    # attachment_dict['resource_owner_id'] = attachment
    # attachment_dict['resource_type'] = attachment
    # attachment_dict['association'] = attachment
    # attachment_dict['bytes_processed_in_gb'] = convert_bytes_to_gb(bytes_processed)
    # attachment_dict['costs_incurred'] = calculated_costs(bytes_processed)
    # attachment_dict['costs_incurred_to_rands'] = calculated_costs_to_rands(bytes_processed, zar_rate)
    # attachment_dict['vatted_costs_incurred_to_rands'] = calculated_vatted_costs_incurred_to_rands(bytes_processed,
    #                                                                                               zar_rate)
    return attachment_dict


def calculated_costs(sum_data):
    bast_cost_data_processed = 0.02
    return bast_cost_data_processed * convert_bytes_to_gb(sum_data)


def calculated_costs_to_rands(sum_data, rate):
    dollar = calculated_costs(sum_data)
    return dollar * rate


def calculated_vatted_costs_incurred_to_rands(sum_data, rate):
    vat = 15
    rands = calculated_costs_to_rands(sum_data, rate)
    return (rands * vat) / 100.0


def fetch_latest_conversion_rate_data():
    exchange_rate_api_url = "https://openexchangerates.org/api/latest.json?app_id=4d9fb3116eaa4ea89998ce4bd239874f"
    try:
        response = requests.get(exchange_rate_api_url)
        converted_response = response.json()
        return converted_response['rates']['ZAR']
    except requests.exceptions.HTTPError as err:
        print('zar conversion error ', err)


def get_previous_month_start_end_date():
    today = datetime.utcnow()
    first = today.replace(day = 1)
    last_day_of_month = first - timedelta(days = 1)
    reset_hours = datetime.combine(last_day_of_month, datetime.min.time())
    return reset_hours.replace(day = 1), reset_hours


def create_date_list(_start_date, _end_date):
    dates = []
    delta = timedelta(days = 1)
    # create date list for three months from today
    while _start_date <= _end_date:
        dates.append(_start_date)
        _start_date += delta
    return dates


def convert_bytes_to_gb(sum_data):
    return sum_data / (1000 * 1000 * 1000)


def boto3_service(client_name, credentials):
    """
    :type client_name: str
    :type credentials: dict
    """
    client = boto3.client(client_name,
                          aws_access_key_id = credentials['ACCESS_KEY'],
                          aws_secret_access_key = credentials['SECRET_KEY'],
                          aws_session_token = credentials['SESSION_TOKEN'],
                          verify = False,
                          region_name = 'eu-west-1'
                          )
    return client


def sts_assume_cross_account_role():
    _cred_role_dict = dict()
    prod_network_acc_id = '033154308392'
    arn_role_cross_account = f"arn:aws:iam::{prod_network_acc_id}:role/BoundedSharedCostsServiceAccountRole"

    sts_connection_lambda_role = boto3.client('sts', region_name = 'eu-west-1')

    acc_master = sts_connection_lambda_role.assume_role(
        RoleArn = arn_role_cross_account,
        RoleSessionName = "cross_acct_role"
    )

    # Temporary credentials consisting of an access key ID, a secret access key, and a security token
    _cred_role_dict['ACCESS_KEY'] = acc_master['Credentials']['AccessKeyId']
    _cred_role_dict['SECRET_KEY'] = acc_master['Credentials']['SecretAccessKey']
    _cred_role_dict['SESSION_TOKEN'] = acc_master['Credentials']['SessionToken']
    return _cred_role_dict
