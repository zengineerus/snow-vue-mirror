import json
import datetime
import config as config
import urllib.request as urllib


class Weather:
    def __init__(self, status_url):
        self.status_url = status_url

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
