from platform_scrapper.utilities.manager import Manager
manager = Manager()
disp = manager.query_maker('61b6808cc2a6e2009ae30fdc').get('cName', None)
