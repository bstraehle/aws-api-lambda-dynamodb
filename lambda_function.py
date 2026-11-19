import boto3
import json
import os
from botocore.exceptions import BotoCoreError, ClientError

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

OPERATIONS = {
    'GET': lambda x: DDB.scan(TableName=TABLE_NAME, **(x or {})),
    'POST': lambda x: DDB.put_item(TableName=TABLE_NAME, **x),
    'PUT': lambda x: DDB.update_item(TableName=TABLE_NAME, **x),
    'DELETE': lambda x: DDB.delete_item(TableName=TABLE_NAME, **x),
}

def respond(err, res=None):
    return {
        'statusCode': 400 if err else 200,
        'body': json.dumps({'error': str(err)}) if err else json.dumps(res),
        'headers': {
            'Content-Type': 'application/json',
        },
    }

def lambda_handler(event, context):
    operation = event['httpMethod']
    if operation not in OPERATIONS:
        return respond(ValueError(f'Unsupported method "{operation}"'))
    try:
        payload = event['queryStringParameters'] if operation == 'GET' else json.loads(event['body'] or '{}')
        return respond(None, OPERATIONS[operation](payload))
    except (BotoCoreError, ClientError, ValueError, TypeError) as err:
        return respond(err)
