import json
THRESHOLD = .94

def lambda_handler(event, context):
   # Grab the inferences from the event
    
    inference = event["body"]["inferences"]

    meets_threshold = inference[0] > THRESHOLD or inference[1] > THRESHOLD
    
    # if max(inferences) > THRESHOLD:
    #     meets_threshold = True 
    # else:
    #     meets_threshold = False
    # print(meets_threshold)
# If our threshold is met, pass our data back out of the
# Step Function, else, end the Step Function with an error
    # meets_threshold = False
    if meets_threshold == True:
        pass
    else:
        raise ValueError("THRESHOLD_CONFIDENCE_NOT_MET")
    
    return {
    'statusCode': 200,
    'body': json.dumps(event)
}