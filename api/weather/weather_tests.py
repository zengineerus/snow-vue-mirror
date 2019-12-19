import unittest
from unittest.mock import MagicMock, patch
from weather.weather import Weather
import urllib.request as urllib
import json


class FakeResponse():
    def read():
        pass

class TestWeather(unittest.TestCase):
    def test_set_status_success(self):
        with patch('urllib.request.urlopen') as urlopen_mock, patch('urllib.request.Request') as urlrequest_mock:
            weather = Weather("fake_url")
            urlrequest_mock.return_value = {"foo": "bar"}

            mock_response = urlopen_mock.return_value
            mock_response.read.return_value = bytearray(
                '{"foo": "bar"}', 'utf-8')
            weather.set_status()
            self.assertEqual(weather.status, {
                "foo": "bar"
            })

    def test_set_status_failure(self):
        with patch('urllib.request.urlopen') as urlopen_mock, patch('urllib.request.Request') as urlrequest_mock:
            weather = Weather("fake_url")
            urlrequest_mock.return_value = "fail"

            mock_response = urlopen_mock.return_value
            mock_response.read.return_value = "fail"

            weather.set_status()
            self.assertEqual(weather.status, {"Error": "Unavailable"})

    def test_get_status_success(self):
        weather = Weather("fake_url")
        status_msg = "Success"
        weather.status = status_msg
        result = weather.get_status()
        self.assertEqual(result, status_msg)

    def test_save_to_dynamo_success(self):
        weather = Weather("fake_url")
        weather.table.put_item = MagicMock()

        expected_data = {
            "overnight": {
                "inches": "5",
                "centimeters": "12.70" 
            },
            "twentyFourHour": {
                "inches": "8",
                "centimeters": "20.32"
            },
            "timestamp": "2019-12-18T12:00:00.000Z",
            "resort": "Keystone"
        }
        
        weather.get_data_to_save = MagicMock(return_value=expected_data)

        # weather.save_weather_report()
        weather.save_to_dynamo()

        weather.table.put_item.assert_called_with(expected_data)

    def test_get_data_to_save_makes_request_and_returns_formatted_data(self):
        weather = Weather("mountainweatherreport.net")
        fake_response = FakeResponse()
        mock_response_data = bytearray('''
        {
            "SnowReportSections": [{ 
                "Depth": { 
                    "Inches": "5",
                    "Centimeters": "12.70" 
                    },
                "Description":"Overnight <br> Snowfall"
            }, {
                "Depth": { 
                    "Inches": "8",
                    "Centimeters": "20.32" 
                    },
                "Description":"24 Hours<br/>Snowfall"
            }]
        }''', 'utf-8')

        expected_value = json.loads(mock_response_data)
        fake_response.read = MagicMock(return_value=mock_response_data) # fake_endpoint_data
        urllib.urlopen = MagicMock(return_value=fake_response)
        urllib.Request = MagicMock(return_value="fake request")

        result = weather.get_data_to_save()

        urllib.Request.assert_called_with("mountainweatherreport.net")
        urllib.urlopen.assert_called_with("fake request")
        self.assertEqual(result, expected_value)
        