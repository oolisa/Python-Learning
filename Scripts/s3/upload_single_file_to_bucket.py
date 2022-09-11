import boto3
s3 = boto3.resource('s3')
s3.meta.client.upload_file('/home/ec2-user/environment/Python-Learning/Scripts/s3/create_s3_bucket.py', 'otdynamic', 'create_s3_bucket.py')

response = print("Bucket has been Uploaded")

