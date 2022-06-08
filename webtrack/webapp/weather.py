import requests

from pprint import pprint

from flask import current_app


def get_weather_by_city(city_name):
    url = "http://api.worldweatheronline.com/premium/v1/weather.ashx"
    params = {
        'q': city_name,
        'key': current_app.config['WEATHER_API'],
        'num_of_days': 1,
        'format': 'json',
        'lang': 'ru',
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        if 'current_condition' in response.json()['data']:
            try:
                return response.json()['data']['current_condition'][0]
            except(IndexError, TypeError):
                return False
    except (requests.RequestException,):
        return False


if __name__ == '__main__':
    weather = get_weather_by_city('Saint-Petersburg')
    pprint(weather)
