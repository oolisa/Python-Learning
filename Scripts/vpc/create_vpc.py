#How to Create VPC using Python Boto3

import boto3

client=boto3.client("ec2")

response = client.create_vpc(
    CidrBlock='10.1.0.0/16',
)

print(response)