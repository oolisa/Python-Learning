import boto3

ec2_boto3=boto3.client("ec2")

ec2_boto3.describe_snapshots(SnapshotId=[
    'snap-00ec26f18cd560c7b'
    ])
