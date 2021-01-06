#!/bin/bash

 if [ -e output/token.tmp ]

then

  mv output/token.tmp output/token.tmp.old

fi



aws sts assume-role --role-arn "arn:aws:iam::029549140631:role/AADAdmUsrRole" --role-session-name AWSCLI-Session --duration-seconds 3600 1> output/token.tmp 2> output/token.tmp.err


if (( $? != 0 ))

then

  echo "Error executing: aws sts assume-role --role-arn "arn:aws:iam::029549140631:role/AADAdmUsrRole" --role-session-name AWSCLI-Session"

  echo ""

  echo "Quitting ..."

  exit

fi



vAK=$(grep AccessKeyId output/token.tmp | cut -d: -f2 | sed 's/\"//g' | sed 's/\,//g' | sed 's/ //g')

vSAK=$(grep SecretAccessKey output/token.tmp |cut -d: -f2 | sed 's/\"//g' | sed 's/\,//g' | sed 's/ //g')

vST=$(grep SessionToken output/token.tmp |cut -d: -f2 | sed 's/\"//g' | sed 's/\,//g' | sed 's/ //g')

echo "Writting to Credentials File...."

echo "[scp]" >> ~/.aws/credentials

echo "aws_access_key_id=$vAK" >> ~/.aws/credentials

echo "aws_secret_access_key=$vSAK" >> ~/.aws/credentials

echo "aws_session_key=$vST" >> ~/.aws/credentials

cat ~/.aws/credentials

chmod u+x output/aws_env.sh

. ./output/aws_env.sh

echo "##AWS token is:"

echo ""

cat output/token.tmp

echo ""

echo "Setting Environment Variables......"



export AWS_ACCESS_KEY_ID=$vAK

export AWS_SECRET_ACCESS_KEY=$vSAK

export AWS_SESSION_TOKEN=$vST

echo "Environment variables have been set!"

