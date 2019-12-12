import urllib.request as urllib
import re
# from api.handlers.library.config import config
import time
import json
import random
import boto3
from boto3.dynamodb.conditions import Key
# import googlemaps

# we don't have an api key yet, returning stub data for now
class googlemaps: 
    def Client(key):
        return googlemaps()

    def distance_matrix(self, origins, destinations):
        return {
           "rows":[{"elements":[{"duration":{"value": random.randint(8000, 10000)}}]}]
        }


class Traffic():
    def __init__(self, resort_location, user_location):
        self.resort_location = resort_location
        self.user_location = user_location

        self.gmaps = googlemaps.Client(key='123235467867543')
        self.dynamo = boto3.resource('dynamodb', region_name='us-east-1')

        # if userLocation and self.validateUse rLocation(userLocation):
        #     self.userLocation = userLocation

    def time_in_hours_and_minutes(self, seconds):
        hours = int(seconds / 3600)
        minutes = int(seconds / 60) % 60

        return {
            "hours": str(hours),
            "minutes": str(minutes)
        }
    
    def get_traffic_data(self):
        try:
            existing_data = self.get_dynamo_data()
            if (existing_data != None and existing_data["time"] > int(time.time()) - 15 * 60):
                self.duration = {
                    "hours": existing_data["hours"],
                    "minutes": existing_data["minutes"]
                }

            else:
                self.make_google_api_call()
        except Exception as e:
            self.duration = 'unavailable'

    def make_google_api_call(self):
        try:
            travel = self.gmaps.distance_matrix([self.user_location], [self.resort_location])
            seconds = travel["rows"][0]["elements"][0]["duration"]["value"]
            self.duration = self.time_in_hours_and_minutes(seconds)
            self.set_dynamo_data(self.make_dynamo_data())
        except Exception as e:
            self.duration = 'unavailable'

    def get_response(self):
        return {
            "travel_time": self.duration,
            "start_location": self.user_location,
            "destination": self.resort_location,
        }

    def make_dynamo_data(self):
        return {
            "identifier": self.user_location + "---" + self.resort_location,
            "hours": self.duration["hours"],
            "minutes": self.duration["minutes"],
            "time": int(time.time())
        }

    def set_dynamo_data(self, data):
        table = self.dynamo.Table("TrafficData")
        table.put_item(Item=data)

    def get_dynamo_data(self):
        table = self.dynamo.Table("TrafficData")

        response = table.query(
            KeyConditionExpression=Key("identifier").eq(self.user_location + "---" + self.resort_location),
            ScanIndexForward=False,
            Limit=1
        )
        try:
            items = response['Items']
            return items[0]
        except:
            return None

#     def validateUserLocation(self):
#         pattern = "\d{1,4} [\w\s]{1,20}(?:street|st|avenue|ave|road|rd|highway|hwy|square|sq|trail|trl|drive|dr|court|ct|park|parkway|pkwy|circle|cir|boulevard|blvd)\W?(?=\s|$)"
#         if re.search(pattern, self.userLocation):
#             return True
#         else:
#             return False
