import unittest
from unittest.mock import MagicMock
from traffic.keystone_traffic import KeystoneTraffic
from boto3.dynamodb.conditions import Key
import boto3


class MockBoto:
  def dynamo():
    pass

class TestKeystoneTraffic(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        mock_boto = MockBoto()
        boto3.resource = MagicMock(return_value=mock_boto)

    def test_keystone_traffic_constructor_sets_user_and_resort_location(self):
        keystone_traffic = KeystoneTraffic("user location here")

        self.assertEqual(keystone_traffic.user_location, "user location here")
        self.assertEqual(keystone_traffic.resort_location,
                         "100 Dercum Square, Keystone, CO 80435")


if __name__ == '__main__':
    unittest.main()
