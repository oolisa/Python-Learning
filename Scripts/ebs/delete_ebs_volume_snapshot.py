import boto3

ec2=boto3.client("ec2")

ec2.delete_snapshot(SnapshotId='snap-01a78c83081755d9b')

response = ec2.delete(SnapshotId='snap-01a78c83081755d9b',
    
    ec2=boto3.client("ec2")
)

print(response)

