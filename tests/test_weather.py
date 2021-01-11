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
        self.week_London_json = {
            "city": {
                "id": 2643743,
                "name": "London",
                "coord": {
                    "lon": -0.1258,
                    "lat": 51.5085
                },
                "country": "GB",
                "population": 0,
                "timezone": 3600
            },
            "cod": "200",
            "message": 0.7809187,
            "cnt": 7,
            "list": [
                {
                    "dt": 1487242800,
                    "temp": {
                        "day": 286.67,
                        "min": 272.78,
                        "max": 286.67,
                        "night": 273.34,
                        "eve": 277.05,
                        "morn": 281.56
                    },
                    "pressure": 972.73,
                    "humidity": 75,
                    "weather": [
                        {
                            "id": 800,
                            "main": "Clear",
                            "description": "sky is clear",
                            "icon": "01d"
                        }
                    ],
                    "speed": 1.81,
                    "deg": 248,
                    "clouds": 0
                },
                {
                    "dt": 1487329200,
                    "temp": {
                        "day": 278.25,
                        "min": 275.04,
                        "max": 278.25,
                        "night": 275.04,
                        "eve": 275.64,
                        "morn": 276.48
                    },
                    "pressure": 966.98,
                    "humidity": 95,
                    "weather": [
                        {
                            "id": 600,
                            "main": "Snow",
                            "description": "light snow",
                            "icon": "13d"
                        }
                    ],
                    "speed": 3.17,
                    "deg": 262,
                    "clouds": 92,
                    "rain": 11.74,
                    "snow": 0.31
                },
                {
                    "dt": 1487415600,
                    "temp": {
                        "day": 277.93,
                        "min": 269.55,
                        "max": 278.37,
                        "night": 269.55,
                        "eve": 273.8,
                        "morn": 274.56
                    },
                    "pressure": 966.06,
                    "humidity": 95,
                    "weather": [
                        {
                            "id": 600,
                            "main": "Snow",
                            "description": "light snow",
                            "icon": "13d"
                        }
                    ],
                    "speed": 0.86,
                    "deg": 244,
                    "clouds": 8,
                    "snow": 0.09
                },
                {
                    "dt": 1487502000,
                    "temp": {
                        "day": 276.41,
                        "min": 267.97,
                        "max": 276.41,
                        "night": 269.77,
                        "eve": 273.57,
                        "morn": 267.97
                    },
                    "pressure": 933.27,
                    "humidity": 0,
                    "weather": [
                        {
                            "id": 800,
                            "main": "Clear",
                            "description": "sky is clear",
                            "icon": "01d"
                        }
                    ],
                    "speed": 1.57,
                    "deg": 142,
                    "clouds": 74
                },
                {
                    "dt": 1487588400,
                    "temp": {
                        "day": 276.28,
                        "min": 271.12,
                        "max": 276.28,
                        "night": 273.12,
                        "eve": 274.52,
                        "morn": 271.12
                    },
                    "pressure": 938.21,
                    "humidity": 0,
                    "weather": [
                        {
                            "id": 600,
                            "main": "Snow",
                            "description": "light snow",
                            "icon": "13d"
                        }
                    ],
                    "speed": 1.79,
                    "deg": 248,
                    "clouds": 88,
                    "rain": 0.93,
                    "snow": 0.38
                },
                {
                    "dt": 1487674800,
                    "temp": {
                        "day": 278.1,
                        "min": 271.73,
                        "max": 278.1,
                        "night": 272.55,
                        "eve": 274.01,
                        "morn": 271.73
                    },
                    "pressure": 945.82,
                    "humidity": 0,
                    "weather": [
                        {
                            "id": 800,
                            "main": "Clear",
                            "description": "sky is clear",
                            "icon": "01d"
                        }
                    ],
                    "speed": 2.19,
                    "deg": 262,
                    "clouds": 25,
                    "snow": 0.01
                },
                {
                    "dt": 1487761200,
                    "temp": {
                        "day": 281.76,
                        "min": 273.21,
                        "max": 281.76,
                        "night": 278.88,
                        "eve": 279.22,
                        "morn": 273.21
                    },
                    "pressure": 945.21,
                    "humidity": 0,
                    "weather": [
                        {
                            "id": 500,
                            "main": "Rain",
                            "description": "light rain",
                            "icon": "10d"
                        }
                    ],
                    "speed": 2.98,
                    "deg": 272,
                    "clouds": 65,
                    "rain": 1.48
                }
            ]
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

    def test_current_pressure_by_city_id_London_equals_1012(self):
        self.weather.data.get_current_weather_by_city_id = Mock(return_value=self.current_London_json)
        self.assertEqual(self.weather.current_pressure_by_city_id(self.city_id_London), 1012)

    def test_current_pressure_by_city_id_Mountain_View_equals_1023(self):
        self.weather.data.get_current_weather_by_city_id = Mock(return_value=self.current_Mountain_View_json)
        self.assertEqual(self.weather.current_pressure_by_city_id(self.city_id_Mountain_View), 1023)

    def test_current_pressure_by_city_id_bad_type_exception_when_float_given(self):
        self.weather.data.get_current_weather_by_city_id = Mock(side_effect=TypeError("Wrong type!"))
        with self.assertRaisesRegex(TypeError, "Wrong type!"):
            self.weather.current_pressure_by_city_id(1.23)

    def test_current_pressure_by_city_id_bad_value_exception_when_invalid_city_id_given(self):
        self.weather.data.get_current_weather_by_city_id = Mock(side_effect=ValueError("Wrong value!"))
        with self.assertRaisesRegex(ValueError, "Wrong value!"):
            self.weather.current_pressure_by_city_id(-111)

    def test_current_humidity_by_city_name_London_greater_than_80(self):
        self.weather.data.get_current_weather_by_city_name = Mock(return_value=self.current_London_json)
        self.assertGreater(self.weather.current_humidity_by_city_name(self.city_name_London), 80)

    def test_current_humidity_by_city_name_Mountain_View_greater_than_99(self):
        self.weather.data.get_current_weather_by_city_name = Mock(return_value=self.current_Mountain_View_json)
        self.assertGreater(self.weather.current_humidity_by_city_name(self.city_name_Mountain_View), 99)

    def test_current_humidity_by_city_name_bad_type_exception_when_list_given(self):
        self.weather.data.get_current_weather_by_city_name = Mock(side_effect=TypeError("Wrong type!"))
        with self.assertRaisesRegex(TypeError, "Wrong type!"):
            self.weather.current_humidity_by_city_name(["a", "b", "c"])

    def test_current_humidity_by_city_name_bad_value_exception_when_invalid_city_name_given(self):
        self.weather.data.get_current_weather_by_city_name = Mock(side_effect=ValueError("Wrong value!"))
        with self.assertRaisesRegex(ValueError, "Wrong value!"):
            self.weather.current_humidity_by_city_name("xyz")

    def test_current_humidity_by_city_id_London_less_than_82(self):
        self.weather.data.get_current_weather_by_city_id = Mock(return_value=self.current_London_json)
        self.assertLess(self.weather.current_humidity_by_city_id(self.city_id_London), 82)

    def test_current_humidity_by_city_id_Mountain_View_less_than_101(self):
        self.weather.data.get_current_weather_by_city_id = Mock(return_value=self.current_Mountain_View_json)
        self.assertLess(self.weather.current_humidity_by_city_id(self.city_id_Mountain_View), 101)

    def test_current_humidity_by_city_id_bad_type_exception_when_list_given(self):
        self.weather.data.get_current_weather_by_city_id = Mock(side_effect=TypeError("Wrong type!"))
        with self.assertRaisesRegex(TypeError, "Wrong type!"):
            self.weather.current_humidity_by_city_id(["a", "b", "c"])

    def test_current_humidity_by_city_id_bad_value_exception_when_invalid_city_id_given(self):
        self.weather.data.get_current_weather_by_city_id = Mock(side_effect=ValueError("Wrong value!"))
        with self.assertRaisesRegex(ValueError, "Wrong value!"):
            self.weather.current_humidity_by_city_id(-111)

    def test_week_temperature_forecast_by_city_name_London_13_52_in_temperatures(self):
        self.weather.data.get_week_weather_by_city_name = MagicMock(return_value=self.week_London_json)
        self.assertIn(13.52, self.weather.week_temperature_forecast_by_city_name(self.city_name_London))

    def tearDown(self):
        self.weather = None

        self.city_name_London = None
        self.city_name_Mountain_View = None
        self.city_id_London = None
        self.city_id_Mountain_View = None
        self.current_London_json = None
        self.current_Mountain_View_json = None
        self.week_London_json = None


if __name__ == '__main__':
    unittest.main()
