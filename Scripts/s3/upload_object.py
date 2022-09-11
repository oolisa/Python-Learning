import boto3

s3 = boto3.client('s3')

filename="search_s3_bucket.py"

with open(filename, 'rb') as data:
    s3.upload_fileobj(data, 'otdynamic3', filename)
    print("Object has been uploaded") 
  