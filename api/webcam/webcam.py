import urllib.request as urllib


class Webcam:
    def __init__(self, webcam_url):
        self.webcam_url = webcam_url
        # self.source_type = source_type
        self.images = []

    def get_image_stream(self):
        return self.images

    def set_image_stream(self, images, type):
        self.images = images

    def get_video_url(self):
        return self.webcam_url

    def image_request(self, url):
        try:
            request = urllib.Request(url)
            response = urllib.urlopen(request)
            if response.status == 200:
                return url
            else:
                return None
        except Exception as e:
            return None
