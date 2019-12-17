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
        "statusCode": status,
        "body": json.dumps(content)
    }
