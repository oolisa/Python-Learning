import boto3

ec2_resource=boto3.resource("ec2")

ec2_resource.create_instances(ImageId='ami-02538f8925e3aa27a',

     InstanceType='t2.micro' ,
     MaxCount=1,
     MinCount=1)
     
     