import json
from traffic.keystone_traffic import KeystoneTraffic


def trafficHandler(event, context):
    content = {}
    keystone = KeystoneTraffic("2300 15th st, Denver, CO, 80202")
    keystone.make_google_api_call()
    try:
        content["TrafficReport"] = keystone.duration
        status = 200
    except Exception:
        content["TrafficReport"] = "Unavailable"
        status = 503

    return {
        "statusCode": status,
        "body": json.dumps(content)
    }
