import unittest
from unittest.mock import patch, Mock
from weather.keystone_weather import KeystoneWeather
from datetime import datetime, timedelta
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

    def test_transform_api_data(self):
        keystone_weather = KeystoneWeather()
        fake_endpoint_data = {
            "SnowReportSections": [
                {
                    "Depth": {
                        "Inches": "5",
                        "Centimeters": "12.70"
                    },
                    "Description": "Overnight <br> Snowfall"
                },
                {
                    "Depth": {
                        "Inches": "8",
                        "Centimeters": "20.32"
                    },
                    "Description": "24 Hour<br/>Snowfall"
                }
                ]
        }

        expected_data = {
            "overnight": {
                "inches": "5",
                "centimeters": "12.70" 
            },
            "twentyFourHour": {
                "inches": "8",
                "centimeters": "20.32"
            },
            "timestamp": datetime.utcnow().isoformat(),
            "resort": "Keystone"
        }

        result = keystone_weather.transform_api_data(fake_endpoint_data)
        self.assertEqual(result["overnight"], expected_data["overnight"])
        self.assertEqual(result["twentyFourHour"], expected_data["twentyFourHour"])
        self.assertEqual(result["resort"], expected_data["resort"])
        self.assertAlmostEqual(datetime.fromisoformat(result["timestamp"]), datetime.fromisoformat(expected_data["timestamp"]), delta=timedelta(seconds=1))

if __name__ == '__main__':
    unittest.main()
