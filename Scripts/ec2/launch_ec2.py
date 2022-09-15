import boto3

ec2_resource=boto3.resource("ec2")

ec2_resource.create_instances(ImageId='ami-02538f8925e3aa27a',

     InstanceType='t2.micro' ,
     MaxCount=1,
     MinCount=1)
   
   
#Spun up ec2 instance with Keypair using boto3.client     
# import boto3
#ec2 = boto3.client('ec2')
#response = ec2.run_instances(
#        ImageId='ami-090fa75af13c156b4',
#        InstanceType='t2.micro',
#.       KeyName='ec2',
#.       MinCount=1,
#        MaxCount=1
)
# response     