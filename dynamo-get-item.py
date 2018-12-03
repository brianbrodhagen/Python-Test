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


dynamodb = getDynamo()
table = getTable('users')

item = {
    'username': 'brianbrodhagen',
    'last_name': 'Brodhagen'
}

print(getItem(item))