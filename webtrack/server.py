from flask import Flask, request

from weather import get_weather_by_city

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello!'


@app.route('/<city>')
def weather(city):
    weather_in_city = get_weather_by_city(city_name=city)
    if weather_in_city:
        return f"In city {city}: temperature {weather_in_city['temp_C']}, humidity {weather_in_city['humidity']}, " \
               f"{weather_in_city['weatherDesc'][0]['value']}"
    else:
        return "Сервис погоды временно не доступен"


if __name__ == '__main__':
    app.run(debug=True)
