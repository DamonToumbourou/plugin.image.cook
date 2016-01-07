from xbmcswift2 import Plugin, xbmcgui
from resources.lib import cook
import pyxbmct.addonwindow as pyxbmct
import os

plugin = Plugin()

@plugin.route('/')
def main_menu():
    """ main menu """
    item = [
        {
            'label': plugin.get_string(30000),
            'path': plugin.url_for('search_first_page', page_num=1),
        }
    ]

    return item


@plugin.route('/search/<page_num>', name='search_first_page')
@plugin.route('/search/<page_num>/<search_keyword>')
def search(page_num, search_keyword=""):
    """ search the recipe collection """
    if not search_keyword:
        search_keyword = plugin.keyboard(default=None, heading='Search Recipes', hidden=False)
   
    result = cook.get_search(page_num, search_keyword)
    
    next_page = 1
    if not page_num:
        next_page = int(page_num) + 1

    item = []
    for i in result:
        item.append({
            'label': i['label'],
            'path': plugin.url_for('get_recipe', url=i['path']),
            'thumbnail': i['thumbnail'],
        })

    item.append({
        'label': 'NEXT PAGE',
        'path': plugin.url_for('search', page_num = next_page, search_keyword=search_keyword),
    })

    
    return item


@plugin.route('/recipe/<url>/')
def get_recipe(url):
    window = Cook('Recipe', 'http://www.taste.com.au/images/recipes/col/2014/01/34998_l.jpg')
    window.doModal()
    del window


class Cook(pyxbmct.AddonDialogWindow):

    def __init__(self, title='', img=''):
        super(Cook, self).__init__(title)
        self.img = img
        self.setGeometry(700, 450, 9, 4)
        self.set_info_controls()
        # connenct a key action (Backspace) to close window.
        self.connect(pyxbmct.ACTION_NAV_BACK, self.close)
        
    def set_info_controls(self):
        #image label
        image_label = pyxbmct.Label('food stuffs')
        self.placeControl(image_label, 5, 0)
        #image
        self.image = pyxbmct.Image(self.img)
        self.placeControl(self.image, 5, 4, 4, 1)

if __name__ == '__main__':
    plugin.run()
