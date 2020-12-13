import json
import requests

from codeguru_profiler_agent import with_lambda_profiler

@with_lambda_profiler()
def lambda_handler(event, context):
    print(context)
    print(event)
    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "hello world",
        }),
    }
