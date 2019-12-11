from api.webcam.webcam import Webcam
import urllib.request as urllib
from datetime import date, timedelta, datetime


class KeystoneWebcam(Webcam):
    def __init__(self):
        resort_stake_cam_url = "https://timecam.tv/mediablock/timestreams/vailresort/keystone-snowcam~640/hour/{date}_{hour}/keystone-snowcam~640_{date}_{hour}_{minute}_00_00.jpg"
        super().__init__(
            resort_stake_cam_url)

    def set_image_array(self):
        self.images = self.build_image_array()

    def round_time(self, time, base=5):
        return round(time/base) * base

    def build_image_array(self, time=datetime.utcnow()):
        start = time - timedelta(days=1)
        stop = time
        images = []
        while start <= stop:
            date = f"{start.year}_{start.month}_{start.day}"
            hour = start.hour
            minute = round_time(start.minute)
            if hour < 10:
                hour = '0' + str(hour)
            if minute < 10:
                minute = '0' + str(minute)

            url = self.webcam_url
            url.format(date=date, hour=hour, minute=minute)
            image = super().image_request(url)
            if image is not None:
                images.append(image)
            start += timedelta(minutes=5)
        return images
