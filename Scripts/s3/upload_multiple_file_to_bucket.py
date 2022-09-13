import boto3
import os
import glob


cwd=os.getcwd()

cwd=cwd+"/Scripts/"
files=glob.glob(cwd+"*.py")
files
for file in files:
    s3_resource=boto3.client("s3")
    s3_resource.upload_file(
    Filename=file,
    Bucket="otdynamic",
    Key=file.split("/")
    )




    





