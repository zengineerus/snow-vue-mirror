import urllib.request as urllib
import json


class Keystone():
    def __init__(self, url):
        self.url = url

    def getData(self):
        request = urllib.Request(self.url)
        response = urllib.urlopen(request)
        response_data = response.read()
        if response_data is None:
            return [{}]
        elif isinstance(response_data, str):
            raise Exception("Bad Type")
        else:
            return json.loads(response_data)
