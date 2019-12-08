import unittest
from unittest.mock import patch, Mock
from Keystone import Keystone
import json


class TestKeystone(unittest.TestCase):
    def test_setStatus_sets_status_when_read_returns_json(self):
        with patch('urllib.request.urlopen') as urlopen_mock, patch('urllib.request.Request') as urlrequest_mock:
            Keystone = Keystone()
            Keystone.statusUrl = "test"
            urlrequest_mock.return_value = "test"

            mock_response = urlopen_mock.return_value
            mock_response.read.return_value = {"key": "value"}
            self.assertEqual(Keystone.setStatus().getSnowReportSections(), {"key":"value"})

    def test_setStatus_raises_exception_when_read_returns_str(self):
        with patch('urllib.request.urlopen') as urlopen_mock, patch('urllib.request.Request') as urlrequest_mock:
            Keystone = Keystone()
            Keystone.statusUrl = "test"
            urlrequest_mock.return_value = "test"

            mock_response = urlopen_mock.return_value
            mock_response.read.return_value = "test"

            with self.assertRaises(Exception) as context:
                Keystone.setStatus()
            self.assertTrue("Unavailable" in str(context.exception))

    def test_setStatus_raises_exception_when_read_returns_none
        with patch('urllib.request.urlopen') as urlopen_mock, patch('urllib.request.Request') as urlrequest_mock:
            Keystone = Keystone()
            Keystone.statusUrl = "test"
            urlrequest_mock.return_value = "test"

            mock_response = urlopen_mock.return_value
            mock_response.read.return_value = None

            with self.assertRaises(Exception) as context:
                Keystone.setStatus()
            self.assertTrue("Unavailable" in str(context.exception))