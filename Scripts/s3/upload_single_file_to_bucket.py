import boto3
s3 = boto3.client('s3')

response = s3.put_object(
    Body='search_s3_bucket.py', 
    Bucket='otdynamic3',
    Key='search_s3_bucket.py',
)

print(response)
 