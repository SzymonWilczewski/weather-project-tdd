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
        try:
            weather = self.data.get_current_weather_by_city_id(city_id)
            return weather["main"]["humidity"]
        except TypeError:
            raise TypeError("Wrong type!")
        except ValueError:
            raise ValueError("Wrong value!")

    def week_temperature_forecast_by_city_name(self, city_name):
        try:
            weather = self.data.get_week_weather_by_city_name(city_name)
            temperature = []
            for day in weather["list"]:
                temperature.append(round(day["temp"]["day"] - 273.15, 2))
            return temperature
        except TypeError:
            raise TypeError("Wrong type!")
        except ValueError:
            raise ValueError("Wrong value!")

    def week_temperature_forecast_by_city_id(self, city_id):
        try:
            weather = self.data.get_week_weather_by_city_id(city_id)
            temperature = []
            for day in weather["list"]:
                temperature.append(round(day["temp"]["day"] - 273.15, 2))
            return temperature
        except TypeError:
            raise TypeError("Wrong type!")
        except ValueError:
            raise ValueError("Wrong value!")

    def week_pressure_forecast_by_city_name(self, city_name):
        try:
            weather = self.data.get_week_weather_by_city_name(city_name)
            pressure = []
            for day in weather["list"]:
                pressure.append(day["pressure"])
            return pressure
        except TypeError:
            raise TypeError("Wrong type!")
        except ValueError:
            raise ValueError("Wrong value!")

    def week_pressure_forecast_by_city_id(self, city_id):
        try:
            weather = self.data.get_week_weather_by_city_id(city_id)
            pressure = []
            for day in weather["list"]:
                pressure.append(day["pressure"])
            return pressure
        except TypeError:
            raise TypeError("Wrong type!")
        except ValueError:
            raise ValueError("Wrong value!")

    def week_humidity_forecast_by_city_name(self, city_name):
        try:
            weather = self.data.get_week_weather_by_city_name(city_name)
            humidity = []
            for day in weather["list"]:
                humidity.append(day["humidity"])
            return humidity
        except TypeError:
            raise TypeError("Wrong type!")
        except ValueError:
            raise ValueError("Wrong value!")

    def week_humidity_forecast_by_city_id(self, city_id):
        try:
            weather = self.data.get_week_weather_by_city_id(city_id)
            humidity = []
            for day in weather["list"]:
                humidity.append(day["humidity"])
            return humidity
        except TypeError:
            raise TypeError("Wrong type!")
        except ValueError:
            raise ValueError("Wrong value!")

    def week_average_temperature_by_city_name(self, city_name):
        try:
            weather = self.data.get_week_weather_by_city_name(city_name)
            temperature = []
            for day in weather["list"]:
                temperature.append(round(day["temp"]["day"] - 273.15, 2))
            return round(sum(temperature) / len(temperature), 2)
        except TypeError:
            raise TypeError("Wrong type!")
        except ValueError:
            raise ValueError("Wrong value!")

    def week_average_temperature_by_city_id(self, city_id):
        try:
            weather = self.data.get_week_weather_by_city_id(city_id)
            temperature = []
            for day in weather["list"]:
                temperature.append(round(day["temp"]["day"] - 273.15, 2))
            return round(sum(temperature) / len(temperature), 2)
        except TypeError:
            raise TypeError("Wrong type!")
        except ValueError:
            raise ValueError("Wrong value!")

    def week_average_pressure_by_city_name(self, city_name):
        try:
            weather = self.data.get_week_weather_by_city_name(city_name)
            pressure = []
            for day in weather["list"]:
                pressure.append(day["pressure"])
            return int(round(sum(pressure) / len(pressure), 0))
        except TypeError:
            raise TypeError("Wrong type!")
        except ValueError:
            raise ValueError("Wrong value!")

    def week_average_pressure_by_city_id(self, city_id):
        try:
            weather = self.data.get_week_weather_by_city_id(city_id)
            pressure = []
            for day in weather["list"]:
                pressure.append(day["pressure"])
            return int(round(sum(pressure) / len(pressure), 0))
        except TypeError:
            raise TypeError("Wrong type!")
        except ValueError:
            raise ValueError("Wrong value!")

    def week_average_humidity_by_city_name(self, city_name):
        try:
            weather = self.data.get_week_weather_by_city_name(city_name)
            humidity = []
            for day in weather["list"]:
                humidity.append(day["humidity"])
            return int(round(sum(humidity) / len(humidity), 0))
        except TypeError:
            raise TypeError("Wrong type!")
        except ValueError:
            raise ValueError("Wrong value!")

    def week_average_humidity_by_city_id(self, city_id):
        try:
            weather = self.data.get_week_weather_by_city_id(city_id)
            humidity = []
            for day in weather["list"]:
                humidity.append(day["humidity"])
            return int(round(sum(humidity) / len(humidity), 0))
        except TypeError:
            raise TypeError("Wrong type!")
        except ValueError:
            raise ValueError("Wrong value!")
