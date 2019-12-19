import json
from weather.keystone_weather import KeystoneWeather


def saveWeatherHandler(event, context):
    keystone = KeystoneWeather()
    keystone.save_weather_report()
