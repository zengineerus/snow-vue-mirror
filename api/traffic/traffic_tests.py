import unittest
from unittest.mock import MagicMock
from api.traffic.traffic import Traffic
import time


class TestTraffic(unittest.TestCase):
  def test_convert_seconds_to_hours_and_minutes(self):
    seconds = 55555
    hours = "15"
    minutes = "25"

    traffic = Traffic("blah", "blah")

    actual = traffic.time_in_hours_and_minutes(seconds)
    expected = {
        "hours": hours,
        "minutes": minutes
    }

    self.assertEqual(actual, expected)

  def test_google_maps_api(self):
    traffic = Traffic("blah, blah", "foo, foo")
    origin = ["foo, foo"]
    destination = ["blah, blah"]
    traffic.gmaps.distance_matrix = MagicMock(return_value={
        "rows": [{"elements": [{"duration": {"value": 55555}}]}]
    })

    traffic.make_google_api_call()
    traffic.gmaps.distance_matrix.assert_called_with(origin, destination)
    self.assertEqual(traffic.duration, {
        "hours": "15",
        "minutes": "25"
    })

  def test_google_maps_api_failure(self):
    traffic = Traffic("blah, blah", "ha, ha")
    traffic.gmaps.distance_matrix = MagicMock(
        side_effect=Exception("stuff's broke"))
    traffic.make_google_api_call()
    self.assertEqual(traffic.duration, "Unavailable")

    actual = traffic.time_in_hours_and_minutes(seconds)
    expected = {
      "hours": hours,
      "minutes": minutes
    }

    self.assertEqual(actual, expected)

  def test_google_maps_api(self):
    traffic = Traffic("blah, blah", "foo, foo")
    origin = ["foo, foo"]
    destination = ["blah, blah"]
    traffic.gmaps.distance_matrix = MagicMock(return_value={
      "rows":[{"elements":[{"duration":{"value":55555}}]}]
    })
    traffic.set_dynamo_data = MagicMock()
    traffic.get_dynamo_data = MagicMock(return_value=None)

    traffic.make_google_api_call()
    
    traffic.gmaps.distance_matrix.assert_called_with(origin, destination)
    self.assertEqual(traffic.duration, {
      "hours": "15",
      "minutes": "25"
    })

  def test_google_maps_api_failure(self):
    traffic = Traffic("blah, blah", "ha, ha")
    traffic.gmaps.distance_matrix = MagicMock(side_effect = Exception("stuff's broke"))
    traffic.set_dynamo_data = MagicMock()
    traffic.get_dynamo_data = MagicMock(return_value=None)
    
    traffic.make_google_api_call()
    
    self.assertEqual(traffic.duration, "unavailable")

  def test_get_Response(self):

    traffic = Traffic("foo", "bar")
    traffic.duration = "10 thousand years"

    expected = {
          "travel_time": "10 thousand years",
          "start_location": "foo",
          "destination": "bar",
        }

    actual = traffic.get_response()

  def test_make_dynamo_data(self):
    traffic = Traffic("foo", "bar")
    traffic.duration = {"hours": "1", "minutes": "30"}
    time.time = MagicMock(return_value=123456789)

    actual = traffic.make_dynamo_data()
    expected = {"identifier": "bar---foo", "hours": "1", "minutes": "30", "time": 123456789 }
    self.assertEqual(actual, expected)

  def test_set_dynamo_data(self):
    traffic = Traffic("foo", "bar")
    test_data = {"test": "data"}
    test_table = TestTable()
    test_table.put_item = MagicMock()
    traffic.dynamo.Table = MagicMock(return_value=test_table)

    traffic.set_dynamo_data(test_data)

    traffic.dynamo.Table.assert_called_with("TrafficData")
    test_table.put_item.assert_called_with(Item=test_data)
    

class TestTable():
  def put_item(Item):
    pass

if __name__ == '__main__':
    unittest.main()
