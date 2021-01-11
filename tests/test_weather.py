import unittest
from unittest.mock import *

from src.weather.weather import Weather


class WeatherTest(unittest.TestCase):
    def setUp(self):
        self.weather = Weather()

        self.city_name_London = "London"
        self.city_name_Mountain_View = "Mountain View"
        self.city_id_London = 2643743
        self.city_id_Mountain_View = 420006353
        self.current_London_json = {
            "coord": {
                "lon": -0.13,
                "lat": 51.51
            },
            "weather": [
                {
                    "id": 300,
                    "main": "Drizzle",
                    "description": "light intensity drizzle",
                    "icon": "09d"
                }
            ],
            "base": "stations",
            "main": {
                "temp": 280.32,
                "pressure": 1012,
                "humidity": 81,
                "temp_min": 279.15,
                "temp_max": 281.15
            },
            "visibility": 10000,
            "wind": {
                "speed": 4.1,
                "deg": 80
            },
            "clouds": {
                "all": 90
            },
            "dt": 1485789600,
            "sys": {
                "type": 1,
                "id": 5091,
                "message": 0.0103,
                "country": "GB",
                "sunrise": 1485762037,
                "sunset": 1485794875
            },
            "id": 2643743,
            "name": "London",
            "cod": 200
        }
        self.current_Mountain_View_json = {
            "coord": {"lon": -122.08, "lat": 37.39},
            "weather": [
                {
                    "id": 800,
                    "main": "Clear",
                    "description": "clear sky",
                    "icon": "01d"
                }
            ],
            "base": "stations",
            "main": {
                "temp": 282.55,
                "feels_like": 281.86,
                "temp_min": 280.37,
                "temp_max": 284.26,
                "pressure": 1023,
                "humidity": 100
            },
            "visibility": 16093,
            "wind": {
                "speed": 1.5,
                "deg": 350
            },
            "clouds": {
                "all": 1
            },
            "dt": 1560350645,
            "sys": {
                "type": 1,
                "id": 5122,
                "message": 0.0139,
                "country": "US",
                "sunrise": 1560343627,
                "sunset": 1560396563
            },
            "timezone": -25200,
            "id": 420006353,
            "name": "Mountain View",
            "cod": 200
        }

    def test_current_temperature_by_city_name_London_almost_equal_7_17(self):
        self.weather.data.get_current_weather_by_city_name = Mock(return_value=self.current_London_json)
        self.assertAlmostEqual(self.weather.current_temperature_by_city_name(self.city_name_London), 7.17)

    def test_current_temperature_by_city_name_Mountain_View_almost_equal_9_4(self):
        self.weather.data.get_current_weather_by_city_name = Mock(return_value=self.current_Mountain_View_json)
        self.assertAlmostEqual(self.weather.current_temperature_by_city_name(self.city_name_Mountain_View), 9.4)

    def test_current_temperature_by_city_name_bad_type_exception_when_boolean_given(self):
        self.weather.data.get_current_weather_by_city_name = Mock(side_effect=TypeError("Wrong type!"))
        with self.assertRaisesRegex(TypeError, "Wrong type!"):
            self.weather.current_temperature_by_city_name(True)

    def test_current_temperature_by_city_name_bad_value_exception_when_invalid_city_name_given(self):
        self.weather.data.get_current_weather_by_city_name = Mock(side_effect=ValueError("Wrong value!"))
        with self.assertRaisesRegex(ValueError, "Wrong value!"):
            self.weather.current_temperature_by_city_name("xyz")

    def test_current_temperature_by_city_id_London_almost_equal_7_17(self):
        self.weather.data.get_current_weather_by_city_id = Mock(return_value=self.current_London_json)
        self.assertAlmostEqual(self.weather.current_temperature_by_city_id(self.city_id_London), 7.17)

    def test_current_temperature_by_city_id_Mountain_View_almost_equal_9_4(self):
        self.weather.data.get_current_weather_by_city_id = Mock(return_value=self.current_Mountain_View_json)
        self.assertAlmostEqual(self.weather.current_temperature_by_city_id(self.city_id_Mountain_View), 9.4)

    def test_current_temperature_by_city_id_bad_type_exception_when_boolean_given(self):
        self.weather.data.get_current_weather_by_city_id = Mock(side_effect=TypeError("Wrong type!"))
        with self.assertRaisesRegex(TypeError, "Wrong type!"):
            self.weather.current_temperature_by_city_id(True)

    def test_current_temperature_by_city_id_bad_value_exception_when_invalid_city_id_given(self):
        self.weather.data.get_current_weather_by_city_id = Mock(side_effect=ValueError("Wrong value!"))
        with self.assertRaisesRegex(ValueError, "Wrong value!"):
            self.weather.current_temperature_by_city_id(-111)

    def test_current_pressure_by_city_name_London_equals_1012(self):
        self.weather.data.get_current_weather_by_city_name = Mock(return_value=self.current_London_json)
        self.assertEqual(self.weather.current_pressure_by_city_name(self.city_name_London), 1012)

    def test_current_pressure_by_city_name_Mountain_View_equals_1023(self):
        self.weather.data.get_current_weather_by_city_name = Mock(return_value=self.current_Mountain_View_json)
        self.assertEqual(self.weather.current_pressure_by_city_name(self.city_name_Mountain_View), 1023)

    def test_current_pressure_by_city_name_bad_type_exception_when_float_given(self):
        self.weather.data.get_current_weather_by_city_name = Mock(side_effect=TypeError("Wrong type!"))
        with self.assertRaisesRegex(TypeError, "Wrong type!"):
            self.weather.current_pressure_by_city_name(1.23)

    def test_current_pressure_by_city_name_bad_value_exception_when_invalid_city_name_given(self):
        self.weather.data.get_current_weather_by_city_name = Mock(side_effect=ValueError("Wrong value!"))
        with self.assertRaisesRegex(ValueError, "Wrong value!"):
            self.weather.current_pressure_by_city_name("xyz")

    def tearDown(self):
        self.weather = None

        self.city_name_London = None
        self.current_London_json = None


if __name__ == '__main__':
    unittest.main()
