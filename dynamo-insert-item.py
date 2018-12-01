import boto3
import csv
import json

def getDynamo():
    return boto3.resource('dynamodb')

def getTable(tablename):
    return dynamodb.Table(tablename)

def getItem(data):
    response = table.get_item(
        Key={
            'username': data['username'],
            'last_name': data['last_name']
        }
    )
    return response['Item']


def insertItem(data):
    table.put_item(
        Item=data
    )
    return getItem(data)
    
dynamodb = getDynamo()
table = getTable('users')

item = {
    'username':'addisonbrodhagen',
    'first_name': 'Addison',
    'last_name': 'Brodhagen',
    'email':'addisonbrodhagen@icloud.com'
}

print(insertItem(item))

#insertItem(item)
# TODO: Read from csv file
# TODO: Convert to JSON object
# TODO: Insert/Update db records
