#!/bin/bash

#. ~/WebstormProjects/work/poc-alerting/cli-tools

if [ -e output/token.tmp ]
then
  mv output/token.tmp output/token.tmp.old
fi

aws --no-verify-ssl --region eu-west-1 sts assume-role --duration-seconds 3600 --role-arn "arn:aws:iam::029549140631:role/AADAdmUsrRole" --role-session-name AWSCLI-Session 1> output/token.tmp 2> output/token.tmp.err

if (( $? != 0 ))
then
  echo "Error executing: aws --region eu-west-1 sts assume-role --role-arn "arn:aws:iam::029549140631:role/AADAdmUsrRole" --role-session-name AWSCLI-Session"
  echo ""
  echo "Quitting ..."
  exit
fi

vAK=$(grep AccessKeyId output/token.tmp |cut -d: -f2 | sed 's/\"//g' | sed 's/\,//g' | sed 's/ //g')
vSAK=$(grep SecretAccessKey output/token.tmp |cut -d: -f2 | sed 's/\"//g' | sed 's/\,//g' | sed 's/ //g')
vST=$(grep SessionToken output/token.tmp |cut -d: -f2 | sed 's/\"//g' | sed 's/\,//g' | sed 's/ //g')

echo "export AWS_ACCESS_KEY_ID=$vAK" > output/aws_env.sh
echo "export AWS_SECRET_ACCESS_KEY=$vSAK" >> output/aws_env.sh
echo "export AWS_SESSION_TOKEN=$vST" >> output/aws_env.sh
chmod u+x output/aws_env.sh
. ./output/aws_env.sh


echo "##CAT AWS token with:"
echo ""
echo "cat token.tmp"
echo ""
echo "##Set environment with:"

echo export AWS_ACCESS_KEY_ID=$vAK
echo export AWS_SECRET_ACCESS_KEY=$vSAK
echo export AWS_SESSION_TOKEN=$vST


echo "Environment variables have been set!"