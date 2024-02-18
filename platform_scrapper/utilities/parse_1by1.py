from platform_scrapper.utilities.manager import Manager
manager = Manager()
disp = manager.query_maker('5eb9e4463836aa00b88a6251').get('cName', None)
