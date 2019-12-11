import unittest
from unittest.mock import patch, Mock, MagicMock
from api.webcam.keystone_webcam import KeystoneWebcam
import json


class TestKeystoneWebcam(unittest.TestCase):
    def test_keystone_webcam_constructor_sets_snow_url(self):
        keystone_webcam = KeystoneWebcam()
        keystone_url = "https://timecam.tv/mediablock/timestreams/vailresort/keystone-snowcam~640/hour/{date}_{hour}/keystone-snowcam~640_{date}_{hour}_{minute}_00_00.jpg"

        self.assertEqual(keystone_webcam.webcam_url, keystone_url)

    def test_set_stream_array_success(self):
        pass

    def test_round_time_success_without_base(self):
        time = 33
        keystone_webcam = KeystoneWebcam()
        result = keystone_webcam.round_time(time)
        self.assertEqual(result, 35)

    def test_round_time_with_rounded_number(self):
        time = 30
        base = 5
        keystone_webcam = KeystoneWebcam()
        result = keystone_webcam.round_time(time, base)
        self.assertEqual(result, 30)

    def test_round_time_with_zero(self):
        time = 0
        base = 5
        keystone_webcam = KeystoneWebcam()
        result = keystone_webcam.round_time(time, base)
        self.assertEqual(result, 0)

    def test_round_time_with_smaller_time(self):
        time = 1
        base = 5
        keystone_webcam = KeystoneWebcam()
        result = keystone_webcam.round_time(time, base)
        self.assertEqual(result, 0)

    def test_build_image_array_success(self):
        keystone_webcam = KeystoneWebcam()
        mock = Mock()
        # mock.side_effect = ['url1',None,'url2']
        keystone_webcam.image_request = MagicMock(
            side_effect=['url1', None, 'url2'])
        keystone_webcam.build_image_array()
        keystone_webcam.image_request.assert_has_calls()

    def test_build_image_array_failure(self):
        pass


if __name__ == '__main__':
    unittest.main()
