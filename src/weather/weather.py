from src.weather.weather_data import WeatherData


class Weather:
    def __init__(self):
        self.data = WeatherData()

    def current_temperature_by_city_name(self, city_name):
        try:
            weather = self.data.get_current_weather_by_city_name(city_name)
            return round(weather["main"]["temp"] - 273.15, 2)
        except TypeError:
            raise TypeError("Wrong type!")
        except ValueError:
            raise ValueError("Wrong value!")

    def current_temperature_by_city_id(self, city_id):
        try:
            weather = self.data.get_current_weather_by_city_id(city_id)
            return round(weather["main"]["temp"] - 273.15, 2)
        except TypeError:
            raise TypeError("Wrong type!")
        except ValueError:
            raise ValueError("Wrong value!")

    def current_pressure_by_city_name(self, city_name):
        try:
            weather = self.data.get_current_weather_by_city_name(city_name)
            return weather["main"]["pressure"]
        except TypeError:
            raise TypeError("Wrong type!")
        except ValueError:
            raise ValueError("Wrong value!")

    def current_pressure_by_city_id(self, city_id):
        try:
            weather = self.data.get_current_weather_by_city_id(city_id)
            return weather["main"]["pressure"]
        except TypeError:
            raise TypeError("Wrong type!")
        except ValueError:
            raise ValueError("Wrong value!")

    def current_humidity_by_city_name(self, city_name):
        try:
            weather = self.data.get_current_weather_by_city_name(city_name)
            return weather["main"]["humidity"]
        except TypeError:
            raise TypeError("Wrong type!")
        except ValueError:
            raise ValueError("Wrong value!")

    def current_humidity_by_city_id(self, city_id):
        raise ValueError("Wrong value!")
