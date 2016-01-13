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
    METHOD_NAME = 'Method'
    title = 'Fish with dill and mandarin sauce'
    sub_title = 'This Asian-inspired fish dish is dressed in a sweet mandarin and dill marinade.'
    prep_time = '0:10'

    method_steps = [
            {
                'step': 'mix the ingredients in the bowl.',
            },
            {
                'step': 'put it in the oven.',
            }
    ]
    
    label = 'Food Picture:'
    image = 'http://www.taste.com.au/images/recipes/col/2014/01/34998_l.jpg'

    window = Cook(title)
    window.set_info(sub_title)
    window.set_recipe_info(prep_time)
    window.set_image(label, image)
    window.set_method(METHOD_NAME, method_steps)
    window.doModal()
    del window


class Cook(pyxbmct.AddonDialogWindow):

    def __init__(self, title=''):
        super(Cook, self).__init__(title)
        self.setGeometry(1050, 650, 9, 4)
        # connenct a key action (Backspace) to close window.
        self.connect(pyxbmct.ACTION_NAV_BACK, self.close)

    def set_info(self, sub_title):
        # recipe sub title
        self.sub_title = sub_title
        sub_title = pyxbmct.Label(sub_title)
        self.placeControl(sub_title, 0, 0, 9, 5)
    
    def set_recipe_info(self, prep_time):
        self.label = pyxbmct.Label('Prep Time: ' + prep_time)
        self.placeControl(self.label, 1, 0)

    def set_method(self, METHOD_NAME, method_steps):
        # display the recipe method - name
        list_label = pyxbmct.Label(METHOD_NAME)
        self.placeControl(list_label, 2.5, 2)
        # add steps to the list
        self.list = pyxbmct.List()
        self.placeControl(self.list, 3, 1.85, 2, 2)
        
        step_num = 1
        for i in method_steps:
            items = ['Step {0}: '.format(step_num) + i['step'] ]
            step_num = step_num + 1
            self.list.addItems(items)

    def set_image(self, label, img):
        # image label
        self.img = img
        label = pyxbmct.Label(label)
        self.placeControl(label, 5, 0)
        #image
        self.image = pyxbmct.Image(self.img)
        self.placeControl(self.image, 6, 1, 3, 2)

if __name__ == '__main__':
    plugin.run()
