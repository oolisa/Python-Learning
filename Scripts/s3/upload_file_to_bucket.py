import boto3

client = boto3.client("s3")
client.upload_file("/home/ec2-user/environment/Python-Learning/Scripts/s3/file.txt", "otdynamic", "home/ec2-user/environment/Python-Learning/Scripts/s3/file.txt")




