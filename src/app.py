import json
import codebase as cb

# import requests


def lambda_handler(event, context):

    input_payload = event['body']
    
    out = cb.process(input_payload)

    return {
        "statusCode": 200,
        "headers": {'Content-type' : 'audio/mpeg'},
        "body": buffer.toString('base64'),
    }