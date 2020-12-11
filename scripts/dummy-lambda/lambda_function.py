import json

def lambda_handler(event, context):
    print "This is my dummy lambda"
    # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
