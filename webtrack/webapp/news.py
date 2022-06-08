import requests
from bs4 import BeautifulSoup


def __get_html_content(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.RequestException:
        return False


def __get_news_from_html_soup(soup):
    news_items = soup.select('ul.list-recent-posts > li')
    result_news = []
    for news in news_items:
        news_title = news.select_one('a').text
        news_url = news.select_one('a')['href']
        news_published = news.select_one('time').text
        result_news.append({
            'title': news_title,
            'url': news_url,
            'published': news_published
        })
    return result_news


def get_news():
    url = 'https://www.python.org/blogs/'
    html_content = __get_html_content(url)
    if html_content:
        soup = BeautifulSoup(html_content, 'html.parser')
        news_list = __get_news_from_html_soup(soup)
        return news_list
    return False


if __name__ == '__main__':
    print(get_news())
