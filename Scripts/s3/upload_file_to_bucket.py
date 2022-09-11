import boto3

s3_resource=boto3.client("s3")
s3_resource.upload_file(
    Filename="upload.png",
    Bucket="otdynamic3",
    Key="uploadtest.png")
    
    


