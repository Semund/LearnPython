from pprint import pprint

import requests

WEATHER_API = "b89a7e190e844a54b0a144114223005"


def weather_by_city(city_name):
    url = "http://api.worldweatheronline.com/premium/v1/weather.ashx"
    params = {
        'q': city_name,
        'key': WEATHER_API,
        'num_of_days': 1,
        'format': 'json',
        'lang': 'ru',
    }

    result = requests.get(url, params=params)
    return result.json()


if __name__ == '__main__':
    weather = weather_by_city('Saint-Petersburg')
    print(weather)
