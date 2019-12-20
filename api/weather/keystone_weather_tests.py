import unittest
from unittest.mock import patch, Mock
from weather.keystone_weather import KeystoneWeather
import json


class TestKeystoneWeather(unittest.TestCase):
    def test_set_status_sets_status_when_read_returns_json(self):
        with patch('urllib.request.urlopen') as urlopen_mock, patch('urllib.request.Request') as urlrequest_mock:
            keystoneWeather = KeystoneWeather()
            keystoneWeather.status_url = "test"
            urlrequest_mock.return_value = "test"

            mock_response = urlopen_mock.return_value
            mock_response.read.return_value = bytearray(
                '{"SnowReportSections": "value"}', 'utf-8')
            keystoneWeather.set_status()
            keystoneWeather.set_snow_report_sections()
            self.assertEqual(
                keystoneWeather.get_snow_report_sections(), "value")

    def test_set_status_raises_exception_when_read_returns_str(self):
        with patch('urllib.request.urlopen') as urlopen_mock, patch('urllib.request.Request') as urlrequest_mock:
            keystoneWeather = KeystoneWeather()
            keystoneWeather.status_url = "test"
            urlrequest_mock.return_value = "test"

            mock_response = urlopen_mock.return_value
            mock_response.read.return_value = "test"

            keystoneWeather.set_status()
            self.assertEqual(keystoneWeather.status, {"Error": "Unavailable"})

    def test_set_status_raises_exception_when_read_returns_none(self):
        with patch('urllib.request.urlopen') as urlopen_mock, patch('urllib.request.Request') as urlrequest_mock:
            keystoneWeather = KeystoneWeather()
            keystoneWeather.status_url = "test"
            urlrequest_mock.return_value = "test"

            mock_response = urlopen_mock.return_value
            mock_response.read.return_value = None

            keystoneWeather.set_status()
            self.assertEqual(keystoneWeather.status, {"Error": "Unavailable"})


if __name__ == '__main__':
    unittest.main()
