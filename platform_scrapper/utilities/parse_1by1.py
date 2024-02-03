from platform_scrapper.utilities.manager import Manager
manager = Manager()
disp = manager.query_maker('5fce8cbb5bfb6b010515ec81').get('cName', None)
