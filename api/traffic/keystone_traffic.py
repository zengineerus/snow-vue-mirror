from api.traffic.traffic import Traffic


class KeystoneTraffic(Traffic):
    def __init__(self, user_location):
        resort_location = "100 Dercum Square, Keystone, CO 80435"
        super().__init__(resort_location, user_location)
