import boto3

ec2 = boto3.client("ec2")
x=ec2.describe_instances()
data=x["Reservations"][0]
data_instance=data["Instances"]
for i in range(len(data_instance)):
    print(f"Instance ID is {data_instance[i]['InstanceId']} ")
    
    

