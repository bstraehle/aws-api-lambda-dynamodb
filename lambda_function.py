import boto3
import json
import os

# For encrypted environment variables, comment out the code below and
# see https://github.com/bstraehle/aws-docs/blob/master/Security/KMS/README.md

#from base64 import b64decode

DDB = boto3.client('dynamodb')
TABLE_NAME = os.environ['TABLE_NAME']

#ENCRYPTED = os.environ['TABLE_NAME']
#DECRYPTED = boto3.client('kms').decrypt(
#    CiphertextBlob=b64decode(ENCRYPTED),
#    EncryptionContext={'LambdaFunctionName': os.environ['AWS_LAMBDA_FUNCTION_NAME']}
#)['Plaintext'].decode('utf-8')
#TABLE_NAME = DECRYPTED

def respond(err, res=None):
    return {
        'statusCode': '400' if err else '200',
        'body': err.message if err else json.dumps(res),
        'headers': {
            'Content-Type': 'application/json',
        },
    }

def lambda_handler(event, context):
    operations = {
        'GET': lambda DDB, x: DDB.scan(TableName=TABLE_NAME, **x) if x else DDB.scan(TableName=TABLE_NAME),
        'POST': lambda DDB, x: DDB.put_item(TableName=TABLE_NAME, **x),
        'PUT': lambda DDB, x: DDB.update_item(TableName=TABLE_NAME, **x),
        'DELETE': lambda DDB, x: DDB.delete_item(TableName=TABLE_NAME, **x),
    }

    operation = event['httpMethod']
    if operation in operations:
        payload = event['queryStringParameters'] if operation == 'GET' else json.loads(event['body'])
        return respond(None, operations[operation](DDB, payload))
    else:
        return respond(ValueError('Unsupported method "{}"'.format(operation)))
