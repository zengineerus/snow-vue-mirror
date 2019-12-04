class DeviceTrackerClient:
     def __init__(self, url="https://networking.internal.wwt.com/connectedDevices"):
         self._url = url

     def pull_in_devices(self):
         data = '''
         { "cidr": "#{cidr}" }
         '''
         response = request.post(self._url, data)
         return json.loads(response)
