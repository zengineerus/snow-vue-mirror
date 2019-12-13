import json
from weather.keystone_weather import KeystoneWeather


def weatherHandler(event, context):
    content = {}
    keystone = KeystoneWeather()
    try:
        content["SnowReport"] = keystone.run_snow_report()
        status = 200
    except Exception:
        content["SnowReport"] = "Unavailable"
        status = 503

    return {
        "body": json.dumps(content),
        "headers": {
          "Access-Control-Allow-Origin": "*",
          "Access-Control-Allow-Credentials": False
        },
        "statusCode": status
    }
