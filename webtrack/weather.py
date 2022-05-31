import requests
from pprint import pprint

import settings


def weather_by_city(city_name):
    url = "http://api.worldweatheronline.com/premium/v1/weather.ashx"
    params = {
        'q': city_name,
        'key': settings.WEATHER_API,
        'num_of_days': 1,
        'format': 'json',
        'lang': 'ru',
    }

    try:
        response = requests.get(url, params=params)
        if response:
            if 'current_condition' in response.json()['data']:
                try:
                    return response.json()['data']['current_condition'][0]
                except(IndexError, TypeError):
                    return False
    except (requests.RequestException,):
        return False
    return False


if __name__ == '__main__':
    weather = weather_by_city('Saint-Petersburg')
    pprint(weather)
