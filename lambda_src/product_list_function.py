import boto3
import os
import json

def handler(event, context):
    # Initialize DynamoDB client
    dynamodb = boto3.resource('dynamodb')

    # Get table name from environment variable
    table_name = os.environ.get('TABLE_NAME')

    table = dynamodb.Table(table_name)

    # Scan the table
    response = table.scan()

    items = response.get('Items', [])

    # Return the items
    return {
        'statusCode': 200,
        'body': json.dumps(items, default=str)
    }
