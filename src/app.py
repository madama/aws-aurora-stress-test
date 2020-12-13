import json
import os
import pymysql



from codeguru_profiler_agent import with_lambda_profiler

@with_lambda_profiler()
def lambda_handler(event, context):
    print(context)
    print(event)
    message = "hello world"
    if (event["queryStringParameters"] and "doIt" in event["queryStringParameters"] and event["queryStringParameters"]["doIt"] == "true"):
        if ("DB_HOST" in os.environ and "DB_USER" in os.environ and "DB_PASSWORD" in os.environ and "DB_NAME" in os.environ):
            host = os.environ["DB_HOST"]
            user = os.environ["DB_USER"]
            password = os.environ["DB_PASSWORD"]
            dbname = os.environ["DB_NAME"]
            conn = pymysql.connect(host, user=user, port=3306, passwd=password, db=dbname)
            message = "Stressed!"

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": message,
        }),
    }


