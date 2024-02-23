from platform_scrapper.src.manager import Manager
manager = Manager()
disp = manager.query_maker('6195e7e9a7493e00a8efe518').get('cName', None)
