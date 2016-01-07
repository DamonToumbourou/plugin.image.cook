from bs4 import BeautifulSoup as bs
import urllib2
import requests 
import re

"""
def get_category(url):
    soup = get_soup(url)
    content = soup.find_all('div', {'class': 'popular-collection clearfix'})
    content = soup.find_all('h2')

    for i in content:
        print i
#get_category('http://www.taste.com.au/')
"""

def get_search(page_num, keyword):
    keyword = keyword.replace(' ', '+')
    SEARCH_URL = 'http://www.taste.com.au/search-recipes/?q=' + keyword + '&page=' + str(page_num) 
    
    html = urllib2.urlopen(SEARCH_URL).read()
    html = html.replace("</scr' + 'ipt>","")
    soup = bs(html, 'html.parser')
    content = soup.find('div', {'class': 'content-item'})
    content = soup.find_all('div', {'class': 'story-block '})
    
    output = []
    for i in content:
        path = i.find('a').get('href')
        
        label = i.get_text().strip()
        try:
            thumb = i.find('img')['src']
            thumb =  thumb.replace('_s', '_l')
            thumb = thumb.replace('_m', '_l')

        except AttributeError:
            continue
    
        item = {
            'label': label,
            'path': path,
            'thumbnail': thumb,
        }

        output.append(item)

    return output
#iget_search(1,'cheese sticks')


def get_recipe(url):
    html = requests.get(url)
    soup = bs(html.text, 'html.parser')

    heading = soup.find('div', {'class': 'heading'})

    print heading

#get_recipe('http://www.taste.com.au/recipes/34861/fish+with+mandarin+and+dill+sauce')
