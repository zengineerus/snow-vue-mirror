import unittest
from unittest.mock import MagicMock
from traffic.traffic import Traffic
import time
from boto3.dynamodb.conditions import Key
import boto3

class MockBoto:
  def dynamo():
    pass

class TestTraffic(unittest.TestCase):
  @classmethod
  def setUpClass(cls):
    mock_boto = MockBoto()
    boto3.dynamo = MagicMock(return_value=mock_boto)

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


  def test_get_response(self):
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
  
  def test_get_dynamo_data_returns_first_item(self):
    traffic = Traffic("foo", "bar")
    test_table = TestTable()
    test_table.query = MagicMock(return_value={"Items":["Item 1", "Item 2"]})
    traffic.dynamo.Table = MagicMock(return_value=test_table)

    actual = traffic.get_dynamo_data()

    test_table.query.assert_called_with(
      KeyConditionExpression=Key("identifier").eq("bar---foo"),
      ScanIndexForward=False,
      Limit=1
    )
    self.assertEqual(actual, "Item 1")

  def test_get_dynamo_data_with_bad_response_returns_none(self):
    traffic = Traffic("foo", "bar")
    test_table = TestTable()
    test_table.query = MagicMock(return_value="blargh")
    traffic.dynamo.Table = MagicMock(return_value=test_table)

    actual = traffic.get_dynamo_data()

    self.assertEqual(actual, None)

  def test_get_traffic_data_skips_gmaps_if_not_needed(self):
    traffic = Traffic("foo", "bar")
    traffic.get_dynamo_data = MagicMock(return_value={"time": time.time(), "hours": "1", "minutes": "75"})
    traffic.make_google_api_call = MagicMock()

    traffic.get_traffic_data()

    traffic.make_google_api_call.assert_not_called()
    self.assertEqual(traffic.duration, {"hours": "1", "minutes": "75"})

  def test_get_traffic_calls_gmaps_if_needed(self):
    traffic = Traffic("foo", "bar")
    traffic.get_dynamo_data = MagicMock(return_value=None)
    traffic.make_google_api_call = MagicMock()

    traffic.get_traffic_data()

    traffic.make_google_api_call.assert_called()

class TestTable():
  def put_item(Item):
    pass
  def query(*args):
    pass

if __name__ == '__main__':
    unittest.main()
