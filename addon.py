from xbmcswift2 import Plugin, xbmcgui

plugin = Plugin()


@plugin.route('/')
def main_menu():
    """ main menu """
    item = [
        {
            'label': plugin.get_string(30000),
            'path': plugin.url_for('search'),
        }
    ]

    return item


@plugin.route('/search/')
def search():
    """ search the recipe collection """
    search_keyword = plugin.keyboard(default=None, heading='Search Recipes', hidden=False)
    
    results = get_search(search_keyword)
    
    
    


if __name__ == '__main__':
    plugin.run()
