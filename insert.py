import json
import boto3

def lambda_handler(event, context):
    # Extract the data from the API Gateway event
    try:
        body = json.loads(event['body'])
        id = body['id']
        name = body['name']
    except KeyError as e:
        return {
            'statusCode': 400,
            'body': json.dumps({'error': 'Invalid input format'})
        }
    
    # Connect to DynamoDB
    dynamodb = boto3.resource('dynamodb')
    table_name = 'UserData'  # Replace with your actual DynamoDB table name
    table = dynamodb.Table(table_name)
    
    # Insert the record into DynamoDB
    try:
        item = {
            'id': id,
            'name': name
        }
        table.put_item(Item=item)
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': 'Failed to insert record into DynamoDB'})
        }
    
    # Return a success response
    return {
        'statusCode': 200,
        'body': json.dumps({'message': 'Record inserted successfully'})
    }