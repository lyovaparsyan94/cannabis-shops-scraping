from platform_scrapper.utilities.manager import Manager
manager = Manager()
disp = manager.query_maker('64a2d5ccd203a500091fa554').get('cName', None)
