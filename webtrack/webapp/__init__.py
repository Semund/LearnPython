from flask import Flask, render_template, flash, redirect, url_for
from flask_login import LoginManager, current_user, login_user, logout_user, login_required

from webapp.weather import get_weather_by_city
from webapp.news import get_news
from webapp.model import db, News, User
from webapp.forms import LoginForm


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    db.init_app(app)

    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'login'

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(user_id)

    @app.route('/')
    @login_required
    def index():
        title = 'News and Weather'
        weather_in_city = get_weather_by_city(city_name=app.config["DEFAULT_CITY"])
        python_news = News.query.order_by(News.published.desc()).all()
        return render_template('index.html', weather=weather_in_city, news=python_news, page_title=title)

    @app.route('/login')
    def login():
        if current_user.is_authenticated:
            return redirect(url_for('index'))

        title = 'Authorization'
        login_form = LoginForm()
        return render_template('login.html', page_title=title, form=login_form)

    @app.route('/process-login', methods=['POST'])
    def process_login():
        form = LoginForm()

        if form.validate_on_submit():
            user = User.query.filter(User.username == form.username.data).first()
            if user and user.check_password(form.password.data):
                login_user(user)
                flash('Вы успешно вошли на сайт')
                return redirect(url_for('index'))
        flash('Неправильные имя или пароль')
        return redirect(url_for('login'))

    @app.route('/logout')
    def logout():
        logout_user()
        return redirect(url_for('login'))

    @app.route('/admin')
    @login_required
    def admin_index():
        if current_user.is_admin:
            return 'Привет, админ'
        return 'Ты не админ'

    return app
