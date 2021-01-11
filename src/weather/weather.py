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
