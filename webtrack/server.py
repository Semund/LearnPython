from flask import Flask, request, render_template

from weather import get_weather_by_city

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello!'


@app.route('/<city>')
def weather(city):
    title = 'Weather'
    weather_in_city = get_weather_by_city(city_name=city)
    return render_template('weather.html', weather=weather_in_city, page_title=title)


if __name__ == '__main__':
    app.run(debug=True)
