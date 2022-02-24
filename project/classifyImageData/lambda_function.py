import json
import base64
import boto3

# Fill this in with the name of your deployed model
ENDPOINT = 'image-classification-2022-02-24-10-46-56-956'
runtime = boto3.client('runtime.sagemaker')

def lambda_handler(event, context):

    # Decode the image data
    image = base64.b64decode(event['body']['image_data'] )

    predictions = runtime.invoke_endpoint(
        EndpointName=ENDPOINT,
        ContentType='image/png',
        Body=image)

    
    inference = json.loads(predictions['Body'].read().decode('utf-8'))
    # event["inferences"] = inference
    # return {
    #     'statusCode': 200,
    #     'body': inference
    # }
    
    
    
    event["body"]["inferences"] = inference
    print(event["body"])
    return {
          "statusCode": 200,
          "body": json.dumps(event["body"])
    }
        
    
    # event["inferences"] = inferences.decode('utf-8')
    # return {
    #     'statusCode': 200,
    #     'body': json.dumps(event)
    # }