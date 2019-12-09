import json
from library.keystone.keystone import keystone as Keystone

#TOPIC: could be two separate lambda
def keystoneHandler(event, context):
    content = {}
    keystone = Keystone(event["queryStringParameters"]["userLocation"])

    try:
        content["SnowReport"] = keystone.runSnowReport()
    except e:
        content["SnowReport"] = "Unavailable"

    try:
        content["TravelTime"] = keystone.runTravelTimeReport()
    except e:
        content["TravelTime"] = "Unavailable"

    if content["SnowReport"] == "Unavailable" and content["TravelTime"] == "Unavailable":
        status = 503
    else:
        status = 200

    return {
        "statusCode": status,
        "body": content
    }