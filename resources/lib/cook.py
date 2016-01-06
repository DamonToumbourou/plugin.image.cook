from bs4 import BeautifulSoup as bs 
import requests 
import re


def get_soup(url):
    page = requests.get(url)
    soup = bs(page.text, 'html.parser')

    return soup


def get_category(url):
    soup = get_soup(url)
    content = soup.find_all('div', {'class': 'popular-collection clearfix'})
    content = soup.find_all('h2')

    for i in content:
        print i
#get_category('http://www.taste.com.au/')


def get_search(keyword):
    SEARCH_URL = 'http://www.taste.com.au/search-recipes/?q=' + keyword  + '&x=0&y=0'
    soup = get_soup(SEARCH_URL)
    content = soup.find('div', {'class': 'content-item'})
    content = soup.find_all('h3')

    for i in content:
        if i.find('a'):
            print 'path: '
            print i
            print '\n\n\n\n\n\n'

get_search('cheese')
