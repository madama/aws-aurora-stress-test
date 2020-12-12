import json

# import requests


def lambda_handler(event, context):
    print(event)
    print(context)
    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "hello world",
        }),
    }
