def handler(event, context):
    print("in handler")
    print(event)
    return {
        'statusCode': 200,
        'body': 'hello, world'
    }
