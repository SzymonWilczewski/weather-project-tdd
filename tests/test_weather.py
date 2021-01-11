import unittest
from unittest.mock import *

from src.weather.weather import Weather


class WeatherTest(unittest.TestCase):
    def setUp(self):
        self.weather = Weather()

        self.city_name_London = "London"
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

    def test_current_temperature_by_city_name_London_almost_equal_7_17(self):
        self.weather.data.get_current_weather_by_city_name = Mock(return_value=self.current_London_json)
        self.assertAlmostEqual(self.weather.current_temperature_by_city_name(self.city_name_London), 7.17)

    def tearDown(self):
        self.weather = None

        self.city_name_London = None
        self.current_London_json = None


if __name__ == '__main__':
    unittest.main()
