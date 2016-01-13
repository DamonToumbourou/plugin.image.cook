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
    html = urllib2.urlopen(url).read()
    html = html.replace("</scr' + 'ipt>","")
    soup = bs(html, 'html.parser')

    title = soup.find('div', {'class': 'heading'})
    title = title.get_text().strip() 
    
    sub_title = soup.find('p', {'class': 'quote-left'})
    sub_title = sub_title.get_text()

    prep_time = soup.find('td', {'class': 'prepTime'})
    prep_time = prep_time.find('em').get_text()

    cook_time = soup.find('td', {'class': 'cookTime'})
    cook_time = cook_time.find('em').get_text()

    ing = soup.find('td', {'class': 'ingredientCount'})
    ing = ing.find('em').get_text()
    
    diff = soup.find('td', {'class': 'difficultyTitle'})
    diff = diff.find('em').get_text()
    
    try:
        serv = soup.find('td', {'class': 'servings'})
        serv = serv.find('em').get_text()
        print serv
    except AttributeError:
        pass

    if not serv:
        serv = soup.find('td', {'class': 'makes'})
        serv = serv.find('em').get_text()
        print serv

    print serv

    img = soup.find('img', {'itemprop': 'photo'})
    img = img.get('src')
    
    output = []
    items = {
            'title': title,
            'sub_title': sub_title,
            'prep_time': prep_time,
            'cook_time': cook_time,
            'ing': ing,
            'diff': diff,
            'serv': serv,
            'img': img,
    }

    output.append(items)
    
    return output
#get_recipe('http://www.taste.com.au/recipes/29331/hazelnut+milk+chocolates')


def get_recipe_method(url):
    html = urllib2.urlopen(url).read()
    html = html.replace("</scr' + 'ipt>","")
    soup = bs(html, 'html.parser')
    step = soup.find_all('p', {'class': 'description'})

    output = []
    for i in step:
        step = i.get_text()
        items = {
            'step': step,
        }

        output.append(items)

    return output
#get_recipe_method('http://www.taste.com.au/recipes/19197/warm+milk+with+a+twist')
