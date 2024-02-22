from platform_scrapper.src.manager import Manager
manager = Manager()
disp = manager.query_maker('60b69a15fa1bf000d21f5601').get('cName', None)
