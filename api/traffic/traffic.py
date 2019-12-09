import urllib.request as urllib
import re
# from api.handlers.library.config import config
import datetime
import json
import random
# import googlemaps

# we don't have an api key yet, returning stub data for now
class googlemaps: 
    def Client(key):
        return googlemaps()

    def distance_matrix(origins, destinations):
        return {
           "rows":[{"elements":[{"duration":{"value": random.randint(8000, 10000)}}]}]
        }


class Traffic():
    def __init__(self, resort_location, user_location):
        self.resort_location = resort_location
        self.user_location = user_location

        self.gmaps = googlemaps.Client(key='123235467867543')
        # if userLocation and self.validateUse rLocation(userLocation):
        #     self.userLocation = userLocation

    def time_in_hours_and_minutes(self, seconds):
        hours = int(seconds / 3600)
        minutes = int(seconds / 60) % 60

        return {
            "hours": str(hours),
            "minutes": str(minutes)
        }

    def make_google_api_call(self):
        try:
            travel = self.gmaps.distance_matrix([self.user_location], [self.resort_location])
            seconds = travel["rows"][0]["elements"][0]["duration"]["value"]
            self.duration = self.time_in_hours_and_minutes(seconds)
        except Exception as e:
            self.duration = {"errawr": str(e)}
#     def validateUserLocation(self):
#         pattern = "\d{1,4} [\w\s]{1,20}(?:street|st|avenue|ave|road|rd|highway|hwy|square|sq|trail|trl|drive|dr|court|ct|park|parkway|pkwy|circle|cir|boulevard|blvd)\W?(?=\s|$)"
#         if re.search(pattern, self.userLocation):
#             return True
#         else:
#             return False

# # TODO: define travel time logic
# # TOPIC: queue then batch process and compile into single API request?

# # Google Maps Distance Matrix API Functions
#     def setTravelUrl(self):
#         if userLocation is None:
#             raise Exception("Unavailable")
#         else:
#             self.travelUrl = "http://maps.googleapis.com/maps/api/distancematrix/json?origins=" + \
#                 self.userLocation + "&destinations=" + \
#                 self.address + "&key=" + config["googleApiKey"]
#         # http://maps.googleapis.com/maps/api/distancematrix/json?origins=Bobcaygeon+ON|24+Sussex+Drive+Ottawa+ON&destinations=2300+15th+St+Denver+CO&key=[YOUR_API_KEY]

# # Invoke setTravelURL(self, userLocation) from child before executing the functions below.
#     def setDistanceMatrixResponse(self):
#         request = urllib.Request(self.travelUrl)
#         response = urllib.urlopen(request)
#         response_data = response.read()
#         if response_data is None or isinstance(response_data, str):
#             raise Exception("Unavailable")
#         else:
#             self.distanceMatrixResponse = json.loads(response_data)

#     def getDistanceMatrixResponse(self):
#         return self.distanceMatrixResponse

#     def storeDistanceMatrixResponse(self):
#         # put maps.gooleapis.com response and user location to DynamoDB
#         print(self.distanceMatrixResponse)

# # Resort Travel Time Functions
#     def setTravelTime(self):
#         self.travelTime = str(datetime.timedelta(
#             self.distanceMatrixResponse["rows"][0]["elements"][0]["duration"]["value"]))

#     def getTravelTime(self):
#         return self.travelTime

#     def storeTravelTime(self):
#         # put travel time and user location to DynamoDB
#         print(self.travelTime)

#     def runTravelTimeReport(self):
#         self.setTravelUrl().setDistanceMatrixResponse().setTravelTime().getTravelTime()
