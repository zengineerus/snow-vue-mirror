from weather.save_weather_handler import saveWeatherHandler
import unittest
from unittest.mock import patch, Mock
import json
from weather.keystone_weather import KeystoneWeather


class TestSaveWeatherHandler(unittest.TestCase):
    def test_save_weather_handler_constructor_success(self):
        pass