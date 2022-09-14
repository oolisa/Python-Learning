#Create snapshot from volume.

#import boto3

#ec2=boto3.client("ec2")

#ec2.create_snapshot( Description='Snapshot from base volume',
     #VolumeId='vol-0cfeab6ffed793721')
     
#How to create AWS EBS volume from Snapshot

import boto3
ec2=boto3.client("ec2")

ec2.create_volume(AvailabilityZone='us-east-1a',
    Encrypted=True,
    Size=12,
    SnapshotId='snap-01a78c83081755d9b',
    VolumeType='gp2')