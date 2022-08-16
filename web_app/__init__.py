from flask import Flask, render_template

from web_app.model import db, News
from web_app.weather import weather_by_city

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    db.init_app(app)

    @app.route('/')
    def index():
        page_title = 'Python news'
        weather = weather_by_city(app.config['WEATHER_DEFAULT_CITY'])
        news_list = News.query.order_by(News.published.desc()).all()
        return render_template('index.html', page_title=page_title, weather=weather, news_list = news_list,
                                weather_city = app.config['WEATHER_DEFAULT_CITY'])
    return app

