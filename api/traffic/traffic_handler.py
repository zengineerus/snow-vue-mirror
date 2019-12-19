import json
from traffic.keystone_traffic import KeystoneTraffic
import urllib


def trafficHandler(event, context):
    content = {}
    try:
        user_location = event["queryStringParameters"]["location"]
    except:
      # user_location = "80202"
        user_location = urllib.parse.quote("2300 15th st, Denver, CO, 80202")

    user_location = urllib.parse.unquote(user_location)
    keystone = KeystoneTraffic(user_location)
    keystone.get_traffic_data()
    
    try:
        content["TrafficReport"] = keystone.get_response()
        status = 200
    except Exception:
        content["TrafficReport"] = "Unavailable"
        status = 503

    return {
        "statusCode": status,
        "body": json.dumps(content),
        "headers": {
            "Access-Control-Allow-Origin": '*',
            "Access-Control-Allow-Credentials": True,
        }
    }
