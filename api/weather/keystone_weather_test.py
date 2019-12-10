import unittest
from unittest.mock import patch, Mock
from weather.keystone_weather import KeystoneWeather
import json


class TestKeystoneWeather(unittest.TestCase):
    def test_setStatus_sets_status_when_read_returns_json(self):
        with patch('urllib.request.urlopen') as urlopen_mock, patch('urllib.request.Request') as urlrequest_mock:
            keystoneWeather = KeystoneWeather()
            keystoneWeather.statusUrl = "test"
            urlrequest_mock.return_value = "test"

            mock_response = urlopen_mock.return_value
            mock_response.read.return_value = bytearray(
                '{"SnowReportSections": "value"}', 'utf-8')
            keystoneWeather.setStatus()
            keystoneWeather.setSnowReportSections()
            self.assertEqual(
                keystoneWeather.getSnowReportSections(), "value")

    def test_setStatus_raises_exception_when_read_returns_str(self):
        with patch('urllib.request.urlopen') as urlopen_mock, patch('urllib.request.Request') as urlrequest_mock:
            keystoneWeather = KeystoneWeather()
            keystoneWeather.statusUrl = "test"
            urlrequest_mock.return_value = "test"

            mock_response = urlopen_mock.return_value
            mock_response.read.return_value = "test"

            with self.assertRaises(Exception) as context:
                keystoneWeather.setStatus()
            self.assertTrue("Unavailable" in str(context.exception))

    def test_setStatus_raises_exception_when_read_returns_none(self):
        with patch('urllib.request.urlopen') as urlopen_mock, patch('urllib.request.Request') as urlrequest_mock:
            keystoneWeather = KeystoneWeather()
            keystoneWeather.statusUrl = "test"
            urlrequest_mock.return_value = "test"

            mock_response = urlopen_mock.return_value
            mock_response.read.return_value = None

            with self.assertRaises(Exception) as context:
                keystoneWeather.setStatus()
            self.assertTrue("Unavailable" in str(context.exception))


if __name__ == '__main__':
    unittest.main()
