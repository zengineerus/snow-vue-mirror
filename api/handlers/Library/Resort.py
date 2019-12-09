import urllib.request as urllib
import json
import datetime
import config
import re

class Resort():
    def __init__(self, statusUrl, address, userLocation):
        self.statusUrl = statusUrl
        self.address = address
        if userLocation and self.validateUserLocation(userLocation):
            self.userLocation = userLocation

    def validateUserLocation(self):
        pattern = "\d{1,4} [\w\s]{1,20}(?:street|st|avenue|ave|road|rd|highway|hwy|square|sq|trail|trl|drive|dr|court|ct|park|parkway|pkwy|circle|cir|boulevard|blvd)\W?(?=\s|$)"
        if re.search(pattern, self.userLocation):
            return True
        else:
            return False

#Resort Status Functions
    def setStatus(self):
        request = urllib.Request(self.statusUrl)
        response = urllib.urlopen(request)
        response_data = response.read()
        if response_data is None or isinstance(response_data, str):
            raise Exception("Unavailable")
        else:
            self.status = json.loads(response_data)

    def getStatus(self):
        return self.status

    def storeStatus(self):
        #store status in dynamoDB
        print(self.status)

#TODO: define travel time logic  
#TOPIC: queue then batch process and compile into single API request?      

#Google Maps Distance Matrix API Functions
    def setTravelUrl(self):
        if userLocation is None:
            raise Exception("Unavailable")
        else:
            self.travelUrl = "http://maps.googleapis.com/maps/api/distancematrix/json?origins=" + self.userLocation + "&destinations=" + self.address + "&key=" + config["apiKey"] 
        #http://maps.googleapis.com/maps/api/distancematrix/json?origins=Bobcaygeon+ON|24+Sussex+Drive+Ottawa+ON&destinations=2300+15th+St+Denver+CO&key=[YOUR_API_KEY]     

#Invoke setTravelURL(self, userLocation) from child before executing the functions below.
    def setDistanceMatrixResponse(self):
        request = urllib.Request(self.travelUrl)
        response = urllib.urlopen(request)
        response_data = response.read()
        if response_data is None or isinstance(response_data, str):
            raise Exception("Unavailable")
        else:
            self.distanceMatrixResponse = json.loads(response_data)        

    def getDistanceMatrixResponse(self):
        return self.distanceMatrixResponse

    def storeDistanceMatrixResponse(self):
        #put maps.gooleapis.com response and user location to DynamoDB
        print(self.distanceMatrixResponse)

#Resort Travel Time Functions
    def setTravelTime(self):
        self.travelTime = str(datetime.timedelta(self.distanceMatrixResponse["rows"][0]["elements"][0]["duration"]["value"]))

    def getTravelTime(self):
        return self.travelTime

    def storeTravelTime(self):
        #put travel time and user location to DynamoDB
        print(self.travelTime)      

    def runTravelTimeReport(self):
        self.setTravelUrl().setDistanceMatrixResponse().setTravelTime().getTravelTime()