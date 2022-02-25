import json
THRESHOLD = .94

def lambda_handler(event, context):
   # Grab the inferences from the event

    
    body = json.loads(event['body'])
    inference = body['inferences']
    
    meets_threshold = inference[0] > THRESHOLD or inference[1] > THRESHOLD
    
    if meets_threshold == True:
        pass
    else:
        raise ValueError("THRESHOLD_CONFIDENCE_NOT_MET")
    
    return {
    'statusCode': 200,
    'body': json.dumps(event)
}