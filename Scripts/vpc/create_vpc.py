#How to Create VPC using Python Boto3

#Method 1 via documentation : 

import boto3

client=boto3.client("ec2")

response = client.create_vpc(
    CidrBlock='10.1.0.0/16',
)

print(response)

#Method 2 without response : 

client.create_vpc(CidrBlock='10.1.0.0/16')
