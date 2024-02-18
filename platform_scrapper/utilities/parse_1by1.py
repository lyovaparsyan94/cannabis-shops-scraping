from platform_scrapper.utilities.manager import Manager
manager = Manager()
disp = manager.query_maker('5edd18b7e41671013eeefa83').get('cName', None)
