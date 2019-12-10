import unittest
from api.traffic.keystone_traffic import KeystoneTraffic

class TestKeystoneTraffic(unittest.TestCase):
  def test_keystone_traffic_constructor_sets_user_and_resort_location(self):
    keystone_traffic = KeystoneTraffic("user location here")

    self.assertEqual(keystone_traffic.user_location, "user location here")
    self.assertEqual(keystone_traffic.resort_location, "100 Dercum Square, Keystone, CO 80435")


if __name__ == '__main__':
    unittest.main()
