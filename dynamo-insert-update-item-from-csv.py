import boto3
from botocore.exceptions import ClientError
import csv

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


def insertUpdateItem(data):
    
    table.put_item(
        Item=data
    )
    return getItem(data)
    

dynamodb = getDynamo()
table = getTable('users')
# TODO: Read from csv file
# TODO: Convert to JSON object
# TODO: Insert/Update db records
try:
    items = []
    with open('names.csv') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',')
        
        for row in reader:
            item = row
           # items.append(row)
           # print(items)
            response = insertUpdateItem(item)
            print(response)
       
    print(f'SUCCESS') 
except ClientError as e:
    print(e.response['Error']['Code'])