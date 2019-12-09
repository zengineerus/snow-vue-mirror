import json
import datetime
import urllib.request as urllib


class Weather():
    def __init__(self, statusUrl, address, userLocation):
        self.statusUrl = statusUrl

# Resort Status Functions
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
        # store status in dynamoDB
        print(self.status)
