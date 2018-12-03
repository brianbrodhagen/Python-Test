import boto3

print('Greetings User...')
#get the service resource

dynamodb = boto3.resource('dynamodb')

#Create the DynamoDb table
table = dynamodb.create_table(
    TableName='users',
    KeySchema=[
       { 
           'AttributeName':'username',
           'KeyType': 'HASH'
       },
       {
           'AttributeName': 'last_name',
           'KeyType': 'RANGE'
       }
    ],
    AttributeDefinitions=[
        {
            'AttributeName' : 'username',
            'AttributeType' : 'S'
        },
        {
            'AttributeName' : 'last_name',
            'AttributeType' : 'S'
        }
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 5,
        'WriteCapacityUnits': 5
    }

)

#wait until the table exists
table.meta.client.get_waiter('table_exists').wait(TableName='users')

print(table.item_count)
print('...end of line')