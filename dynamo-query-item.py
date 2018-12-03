import boto3
from boto3.dynamodb.conditions import Key, Attr
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

def queryDb(q):
    data = {}
    response = table.query(
        KeyConditionExpression=Key('username').eq(q)
    )
    #response['Count']
    #response['Items']

    if ('Items' in response.keys()):
        data = response['Items']
    if('Count' in response.keys()):
        print(response['Count'])
    return data

def getAllItems():
    items = []
    try:
        response = table.scan()

        if ('Items' in response.keys()):
            items = response['Items']
       
    except:
        print('Error')
    return items


dynamodb = getDynamo()
table = getTable('users')

#db_response = queryDb('brianbrodhagen')
items = getAllItems()

for item in items:
    print(item['username'])
