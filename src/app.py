import json
import os
import pymysql
import sys


from codeguru_profiler_agent import with_lambda_profiler

@with_lambda_profiler()
def lambda_handler(event, context):
    #print(context)
    #print(event)
    message = "hello world"
    if (event["queryStringParameters"] and "doIt" in event["queryStringParameters"] and event["queryStringParameters"]["doIt"] == "true"):
        if ("DB_HOST" in os.environ and "DB_USER" in os.environ and "DB_PASSWORD" in os.environ and "DB_NAME" in os.environ):
            try:
                host = os.environ["DB_HOST"]
                user = os.environ["DB_USER"]
                password = os.environ["DB_PASSWORD"]
                dbname = os.environ["DB_NAME"]
                print(host, user, password, dbname)
                conn = pymysql.connect(host, user=user, port=3306, passwd=password, db=dbname)
                cursor = conn.cursor()                                    
                cursor.execute("call eat_cpu(10000);")
                for result in cursor.fetchall():
                    print(result)
                message = "Stressed!"
            except:
                print(print("Unexpected error:", sys.exc_info()[0]))
                raise

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": message,
        }),
    }


