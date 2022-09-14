import boto3

client=boto3.client("ec2")

response = client.delete_vpc(
    VpcId = 'vpc-0a31f2623f9eed763'
    
)

print("VPC Has been removed" , response)
