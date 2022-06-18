from datetime import datetime

import requests
from bs4 import BeautifulSoup
from flask import current_app

from webapp.model import db, News

def __get_html_content(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.RequestException:
        return False


def __get_news_from_html_soup(soup):
    news_items = soup.select('ul.list-recent-posts > li')
    for news in news_items:
        news_title = news.select_one('a').text
        news_url = news.select_one('a')['href']
        news_published = news.select_one('time')['datetime']
        print(news_published)
        try:
            news_published = datetime.strptime(news_published, '%Y-%m-%d')
        except ValueError:
            news_published = datetime.now()

        save_news(news_title, news_url, news_published)


def get_news():
    url = current_app.config['URL_NEWS']
    html_content = __get_html_content(url)
    if html_content:
        soup = BeautifulSoup(html_content, 'html.parser')
        __get_news_from_html_soup(soup)
    return False


def save_news(title, url, published):
    news_exist = News.query.filter(News.url == url).count()
    if not news_exist:
        new_news = News(title=title, url=url, published=published)
        db.session.add(new_news)
        db.session.commit()


if __name__ == '__main__':
    print(get_news())
