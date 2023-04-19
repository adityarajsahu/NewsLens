import requests
from bs4 import BeautifulSoup
import re

# URLs of news websites to be scrapped.
ENGLISH_NEWS = 'https://news-decoder.com/category/world/'
ARABIC_NEWS = 'https://arabic-media.com/articles/id/news-dynamic.php'
FARSI_NEWS = 'https://ir.voanews.com/z/1696'
TURKISH_NEWS = ''


def scrape_english_news(url=ENGLISH_NEWS):
    r = requests.get(url)
    html_content = r.content
    # print(html_content)

    soup = BeautifulSoup(html_content, 'html.parser')
    article_anchor_tags = soup.select('article > h2 > a')
    dates_span_tags = soup.select('.published')
    # print(dates_span_tags[0])

    list_of_dict = []
    for i in range(len(article_anchor_tags) - 1):
        headline_pattern = r">(.*?)<"
        headline = re.findall(headline_pattern, str(article_anchor_tags[i + 1]))[0]

        article_url_pattern = r'"(.*?)"'
        article_url = re.findall(article_url_pattern, str(article_anchor_tags[i + 1]))[0]

        date_pattern = r">(.*?)<"
        date = re.findall(date_pattern, str(dates_span_tags[i + 1]))[0]

        list_of_dict.append({
            'headline': headline,
            'article_url': article_url,
            'date': date,
            'website_url': ENGLISH_NEWS
        })
        
    # print(list_of_dict[0])
    return list_of_dict


def scrape_arabic_news(url=ARABIC_NEWS):
    pass

def scrape_farsi_news(url=FARSI_NEWS):
    pass

def scrape_turkish_news(url=TURKISH_NEWS):
    pass

scrape_english_news()