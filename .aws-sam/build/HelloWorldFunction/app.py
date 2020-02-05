import json
from __future__ import unicode_literals
import codebase as cb

# import requests


def lambda_handler(event, context):

    input_payload = json.loads(event['body'])
    
    out = cb.process(input_payload)

    return {
        "statusCode": 200,
        "body": json.dumps({            
        "message": json.dumps(out)
        }),
    }