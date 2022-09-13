
import boto3

vpc = boto3.client("ec2")

#how to describe all available vpc in account.

response = vpc.describe_vpcs(
    VpcIds=[
        'vpc-0e0f35f82311176d8',
    ],
)

print(response)