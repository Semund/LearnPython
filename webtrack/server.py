from flask import Flask, render_template

from weather import get_weather_by_city
from news import get_news

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello!'


@app.route('/<city>')
def weather(city):
    title = 'Weather'
    weather_in_city = get_weather_by_city(city_name=city)
    python_news = get_news()
    return render_template('weather.html', weather=weather_in_city, news=python_news, page_title=title)


if __name__ == '__main__':
    app.run(debug=True)
