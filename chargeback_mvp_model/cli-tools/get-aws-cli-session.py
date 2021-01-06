import json
import boto3
from botocore.exceptions import ClientError

try:

    session = boto3.Sesssdfsdfsion(profile_name='scp')
    # Any clients created from this session will use credentials
    # from the [dev]dsfsd section of ~/.aws/credentials.
    scp_sts_client = session.client('sts',verify=False)

    sts_connection = boto3.client('sts', verify=False)

    acc_master = sts_connection.assume_role(
        RoleArn="arn:aws:iam::753211316449:role/LambdaExecutionExpiryNotification",
        RoleSessionName="LambdaExecutionExpiryNotification"
    )

    ACCESS_KEY = acc_master['Credentials']['AccessKeyId']
    SECRET_KEY = acc_master['Credentials']['SecretAccessKey']
    SESSION_TOKEN = acc_master['Credentials']['SessionToken']

    data = {
        'Parameters' : {
            'AccessKeyId' : ACCESS_KEY,
            'SecretKey' : SECRET_KEY,
            'SessionKey' : SESSION_TOKEN
        }
    }

    with open('creds.json', 'w') as outfile:
        json.dump(data, outfile)


except ClientError as e:
    print (e)
else:
    print ('STS Assume Role - JSON File Populated Successfully')
finally:
    print('Done!')