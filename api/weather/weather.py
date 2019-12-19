import json
import datetime
import urllib.request as urllib
import config as config
import boto3
from boto3.dynamodb.conditions import Key

class Weather:
    def __init__(self, status_url):
        self.status_url = status_url
        dynamo = boto3.resource('dynamodb', region_name='us-east-1')
        self.table = dynamo.Table("WeatherData")


# Resort Status Functions
    def set_status(self):
        try:
            request = urllib.Request(self.status_url)
            response = urllib.urlopen(request)
            response_data = response.read()
            # if response_data is None or isinstance(response_data, str):
            #     self.status = {"Error": "Unavailable"}
            # else:
            self.status = json.loads(response_data)
        except Exception as e:
            print(e)
            self.status = {"Error": "Unavailable"}

    def get_status(self):
        return self.status

    def store_status(self):
        # store status in dynamoDB
        print(self.status)

    def get_data_to_save(self):
        request = urllib.Request(self.status_url)
        response = urllib.urlopen(request)
        response_data = response.read()
        return json.loads(response_data)
    
    def save_to_dynamo(self):
        resort_weather_data = self.get_data_to_save()
        self.table.put_item(resort_weather_data)