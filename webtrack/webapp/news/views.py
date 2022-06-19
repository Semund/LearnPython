from flask import Blueprint, current_app, render_template
from flask_login import login_required

from webapp.weather import get_weather_by_city
from webapp.news.models import News

blueprint = Blueprint('news', __name__)


@blueprint.route('/')
@login_required
def index():
    title = 'News and Weather'
    weather_in_city = get_weather_by_city(city_name=current_app.config["DEFAULT_CITY"])
    python_news = News.query.order_by(News.published.desc()).all()
    return render_template('news/index.html', weather=weather_in_city, news=python_news, page_title=title)
