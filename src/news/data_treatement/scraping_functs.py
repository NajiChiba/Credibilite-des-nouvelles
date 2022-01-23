import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException, ElementNotInteractableException
import time
import elasticsearch
from elasticsearch_dsl import Search
import pathlib

def add_data_to_elastic(title, content, fake):
    INDEX_NAME = 'news-dt'

    ELASTIC_HOST = 'http://localhost:9200/'

    client = elasticsearch.Elasticsearch(hosts=[ELASTIC_HOST])

    data_1 = {
        'title': title,
        'body': content,
        'fake': fake,
    }

    client.index(index= INDEX_NAME, body= data_1)


def load_more_data(url, button):
    b = webdriver.Chrome(executable_path='D:/chromedriver.exe')

    #url = "https://ar.hibapress.com/covidmaroc.html"

    b.get(url)

    btn = b.find_element_by_id(button)

    for i in range(30):
        try:
            time.sleep(6)
            btn = b.find_element_by_id(button)
            btn.click()
        except ElementClickInterceptedException:
            print("error")

    return b.page_source


#loaded_page_html = load_more_data("https://ar.hibapress.com/covidmaroc.html", 'load-more-archives')
loaded_page_html =""

class Db_conn():
    def __init__(self):
        client = MongoClient()
        self.db = client['news_project']
        self.new_coll = self.db.new

    def insert_elem(self, article):
        result = self.new_coll.insert_one(article)

        print("\n\n\n----------------------")
        print("First article key is: {}".format(result.inserted_id))
        print("----------------------\n\n\n")

    def test(self):
        print(self.db)


db = Db_conn()

def hiba_press_articles(link):

    articles = requests.get(link)

    html_article = articles.text

    soup = BeautifulSoup(html_article, 'html.parser')

    title = soup.find('h1', class_='post-title entry-title').text
    #print("***************** title ******************")
    #print(title)

    ps = list(soup.find('div', class_='entry-content entry clearfix').findAll('p'))
    del ps[3:]

    article=""
    #print("***************** PS ******************")

    for p in ps:
        print(p.string)
        try:
            article = article +" "+ p.string
        except:
            print("cannot concatenate")

    #print("*************** Article ***************")
    #print(article)

    new_elem={
        "title": title,
        "body": article,
        "fake": 0
    }

    print("--------------")

    print(new_elem)

    print("--------------")
    db.insert_elem(new_elem)
    add_data_to_elastic(title, article, 0)


def scraping_hiba_press():
    soup = BeautifulSoup(loaded_page_html, 'html.parser')
    elems = list(soup.find('ul', class_='posts-items').findAll('h2'))
    j = 0
    for i in elems:
        try:
            hiba_press_articles("https://ar.hibapress.com/" + i.contents[0]['href'])
            print("One is executed")
        except:
            hiba_press_articles(i.contents[0]['href'])
            print("Two is executed")

        j = j + 1
        print(j)
        print(len(elems))




def load_more_Fdata(url, button):
    b = webdriver.Chrome(executable_path='D:/chromedriver.exe')

    #url = "https://ar.hibapress.com/covidmaroc.html"

    b.get(url)

    for i in range(48):
        print(i)
        try:
            time.sleep(5)
            btn = b.find_element_by_class_name('w-btn.us-btn-style_5')
            btn.click()
        except (ElementClickInterceptedException, ElementNotInteractableException):
            print("error")

    return b.page_source


'''fn_url = 'https://fatabyyano.net/?s=+%D9%83%D9%88%D8%B1%D9%88%D9%86%D8%A7'
fn_btn = 'w-btn.us-btn-style_5'
fake_news = load_more_Fdata(fn_url, fn_btn)'''

def fatabayanou_scraping():
    #https://fatabyyano.net/?s=+%D9%83%D9%88%D8%B1%D9%88%D9%86%D8%A7

    soup=BeautifulSoup(fake_news,'html.parser')

    articles = soup.find_all('article')

    for art in articles:
        head = art.find('h2',class_='w-post-elm post_title usg_post_title_1 entry-title color_link_inherit')
        link = head.find('a', href=True)

        nextpage = requests.get(link.get('href'))
        print(nextpage)
        soupnext = BeautifulSoup(nextpage.content, 'html.parser')
        title = soupnext.find('h1',class_='w-post-elm post_title us_custom_d6b5cf89 entry-title color_link_inherit')

        try:
            title = title.text
            con = soupnext.find('div', class_='w-post-elm post_content')
            contentList = []
            for par in con.find_all('p'):
                paragraph = par.text
                contentList.append(paragraph)
                content = ' '.join(contentList)
        except:
            print("error --")

        new_element = {"title": title, "body": content, "fake":1}
        db.insert_elem(new_element)
        add_data_to_elastic(title, content, 1)


def scrap_taakad(i):
    html = requests.get(
        'https://www.verify-sy.com/contents/49/%D9%88%D8%A8%D8%A7%D8%A1-%D9%83%D9%88%D8%B1%D9%88%D9%86%D8%A7?page=' + str(
            i))

    soup = BeautifulSoup(html.content, 'html.parser')

    articles = soup.find_all('div', class_='blog_post_style2')

    for art in articles:
        head = art.find('h3', class_='list-title-ca')
        link = head.find('a', href=True)

        nextpage = requests.get(link.get('href'))
        print(nextpage)
        soupnext = BeautifulSoup(nextpage.content, 'html.parser')

        div_title = soupnext.find('div', class_='blog_post_style2_content wow fadeInUp sdfsdfsdf')
        title = div_title.find('h3')

        title = title.text
        con = soupnext.find('div', class_='wekek')
        contentList = []
        for par in con.find_all('p'):
            spans = par.find_all('span')
            for span in spans:
                paragraph = span.text
                contentList.append(paragraph)
                content = ' '.join(contentList)

        new_element = {"title": title, "body": content, "fake": 1}
        print(new_element)
        db.insert_elem(new_element)
        add_data_to_elastic(title, content, 1)


for i in range(12, 17):
    scrap_taakad(i)

#Start scrapping

#fatabayanou_scraping()