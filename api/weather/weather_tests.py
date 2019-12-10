import unittest
from unittest.mock import MagicMock, patch
from api.weather.weather import Weather


class TestWeather(unittest.TestCase):
    def test_set_status_success(self):
        with patch('urllib.request.urlopen') as urlopen_mock, patch('urllib.request.Request') as urlrequest_mock:
            weather = Weather("fakeUrl")
            urlrequest_mock.return_value = {"foo": "bar"}

            mock_response = urlopen_mock.return_value
            mock_response.read.return_value = bytearray(
                '{"foo": "bar"}', 'utf-8')
            weather.set_status()
            self.assertEqual(weather.status, {
                "foo": "bar"
            })

    def test_set_status_failure(self):
        weather = Weather("fakeUrl")
