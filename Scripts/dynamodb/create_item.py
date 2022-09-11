import boto3

dynamodb = boto3.client("dynamodb")

response = dynamodb.put_item(
    Item={
        'ID':{
            'S': 'ded56edc-987d-4044-9282-9051bf0432ff'
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
