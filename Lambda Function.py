import json
import math

# import the AWS SDK
import boto3
from time import gmtime, strftime

# create a DynamoDB object using the AWS SDK
dynamodb = boto3.resource('dynamodb')

table = dynamodb.Table('TwoPointOhDatabase')

now = strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())

# define the handler function that the Lambda service will use as an entry point
def lambda_handler(event, context):

    lat1 = float(event['lat1'])
    lon1 = float(event['lon1'])
    lat2 = float(event['lat2'])
    lon2 = float(event['lon2'])

    lat1_rad = math.radians(lat1)
    lon1_rad = math.radians(lon1)
    lat2_rad = math.radians(lat2)
    lon2_rad = math.radians(lon2)

# calculate the distance in kilometers using the Haversine formula
    dlon = lon2_rad - lon1_rad
    dlat = lat2_rad - lat1_rad
    a = math.sin(dlat / 2)**2 + math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(dlon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    distance = 6371 * c  # Earth's radius in km

# write result and time to the DynamoDB table
    response = table.put_item(
        Item={
            'ID': str(distance),
            'LatestGreetingTime':now
            })


    return {
        'statusCode': 200,
        'body': json.dumps('Your result is ' + str(distance) + ' km')
    }