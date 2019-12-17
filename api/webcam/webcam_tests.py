import unittest
from unittest.mock import patch
from webcam.webcam import Webcam


test_url = "http://testing.com"


class TestWebcam(unittest.TestCase):
    def test_get_image_stream_success(self):
        webcam = Webcam(test_url)
        webcam.images = []
        result = webcam.get_image_stream()
        self.assertEqual(result, [])

    def test_set_image_stream_success(self):
        webcam = Webcam(test_url)
        test_image = [{"img": "test"}]
        webcam.set_image_stream(test_image, "jpg")
        result = webcam.images
        self.assertEqual(result, test_image)

    def test_get_video_url_successfully(self):
        pass

    def test_image_request_success(self):
        pass
