import boto3

dynamodb = boto3.client("dynamodb")

response = dynamodb.put_item(
    Item={

        'ID':{
            'S': 'f92966bb-bc96-4d5c-b63c-92fb5259c9e2'
        },
        
        'AlbumTitle': {
            'S': 'Somewhat Famous',
        },
        'Artist': {
            'S': 'No One You Know',
        },
        'Song': {
            'S': 'Call Me Today',
        },
    },
    ReturnConsumedCapacity='TOTAL',
    TableName='Music',
)

print(response)
