# mport urllib.request
import unittest
from unittest.mock import patch, Mock, MagicMock
from keystone.keystone import Keystone
import json


class TestKeystone(unittest.TestCase):
    def test_getData_returns_not_empty(self):
        url = "https://www.keystoneresort.com/api/PageApi/GetWeatherDataForHeader"
        self.assertNotEqual(Keystone(url).getData(), "")

    def test_x(self):
        with patch('urllib.request.urlopen') as urlopen_mock:
            mock_response = urlopen_mock.return_value
            mock_response.read.return_value = "test"

            with self.assertRaises(Exception) as context:
                Keystone("https://www.testurl.com").getData()
            self.assertTrue("Bad Type" in str(context.exception))
