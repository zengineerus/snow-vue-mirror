import json
import datetime
import urllib.request as urllib
import boto3
from boto3.dynamodb.conditions import Key
from abc import abstractmethod

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

    def get_weather_data(self):
        #get data from dynamo using self.resort_name
        #returning the most recently saved data
        dynamo_report = self.table.query(
            KeyConditionExpression=Key("resort").eq(self.resort_name),
            ScanIndexForward=False,
            Limit=1
        )
        snow_data = None
        # ["Items"][0]
        try:    
            snow_data = dynamo_report["Items"][0]
        except Exception as e:
            snow_data = None
        
        return snow_data

    def get_data_to_save(self):
        request = urllib.Request(self.status_url)
        response = urllib.urlopen(request)
        response_data = response.read()
        return json.loads(response_data)
    
    def save_to_dynamo(self, data):
        self.table.put_item(data)

    @abstractmethod
    def transform_api_data(self, data):
        pass

    def save_weather_report(self):
        data_to_save = self.get_data_to_save()
        transformed_data = self.transform_api_data(data_to_save)
        self.save_to_dynamo(transformed_data)
        