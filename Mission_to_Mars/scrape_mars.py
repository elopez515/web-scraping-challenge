# Import Python Modules
from splinter import Browser
from bs4 import BeautifulSoup as bs
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time

data = {}


def scrape_all():
    # Initiate headless driver for deployment
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    # Go to the NASA Mars News Site 
    url = 'https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'
    browser.visit(url)

    # Create a Beautiful Soup object
    soup = bs(browser.html, 'lxml')

    news_title = soup.find_all('div', class_ = 'content_title')
    news_articles = []
    for news in news_title:
        if (news.a):
            if (news.a.text):
                news_articles.append(news.a.text)

    # Print paragraph for the latest news article
    news_story = soup.find_all('div', class_ = 'article_teaser_body')
    news_paragraph = []
    for paragraph in news_story:
        if (paragraph.text):
            news_paragraph.append(paragraph.text)

    # Create variables for our latest news article and paragraph
    first_article = news_articles[0]
    news_p = news_paragraph[0]
    data["news_title"] = first_article
    data["news_paragraph"] = news_p


    browser.quit()

    return data
