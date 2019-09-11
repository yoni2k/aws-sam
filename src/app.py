import boto3
import json
import os

print('Loading function')

# connect to a dynamo db in given region, 2 environment variables are given
region_name = os.environ['REGION_NAME']
dynamo = boto3.client('dynamodb', region_name=region_name)
table_name = os.environ['TABLE_NAME']

# Called in handler below
def respond(err, res=None):
    # returns a JSON format file with 200 and res received from lambda_handler below
    return {
        'statusCode': '400' if err else '200',
        'body': err.message if err else json.dumps(res),
        'headers': {
            'Content-Type': 'application/json',
        },
    }

def lambda_handler(event, context):
    print("Received event: " + json.dumps(event, indent=2))
    # Return scan of the dynamodb table
    scan_result = dynamo.scan(TableName=table_name)
    return respond(None, res=scan_result)
