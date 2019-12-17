import unittest
from unittest.mock import MagicMock
from traffic.traffic import Traffic


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

    def test_get_response(self):
        traffic = Traffic("foo", "bar")
        traffic.duration = "10 thousand years"

        expected = {
            "travel_time": "10 thousand years",
            "start_location": "foo",
            "destination": "bar",
        }

        actual = traffic.get_response()


if __name__ == '__main__':
    unittest.main()
