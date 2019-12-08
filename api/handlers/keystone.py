import json
from Library.Keystone.Keystone import Keystone

#TOPIC: could be two separate lambda
def keystoneHandler(event, context):
    content = {}
    keystone = Keystone()

    try:
        content["SnowReport"] = keystone.setStatus().setSnowReportSections().getSnowReportSections()
    except e:
        content["SnowReport"] = "Unavailable"

    try:
        content["TravelTime"] = keystone.setTravelUrl(event.body.userLocation).setDistanceMatrixResponse().setTravelTime().getTravelTime() 
    except e:
        content["TravelTime"] = "Unavailable"

    if content["SnowReport"] == "Unavailable" and content["TravelTime"] == "Unavailable":
        status = 503
    else:
        status = 200

    return {
        'statusCode': status,
        'body': content
    }