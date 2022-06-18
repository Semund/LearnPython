from flask import Flask, render_template

from webapp.weather import get_weather_by_city
from webapp.news import get_news
from webapp.model import db, News


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    db.init_app(app)

    @app.route('/')
    def index():
        title = 'News and Weather'
        weather_in_city = get_weather_by_city(city_name=app.config["DEFAULT_CITY"])
        python_news = News.query.order_by(News.published.desc()).all()
        return render_template('weather.html', weather=weather_in_city, news=python_news, page_title=title)

    return app
