from platform_scrapper.utilities.manager import Manager
import shutil
manager = Manager()
disp = manager.query_maker('5fc5762bd9d0e500abb94e2b').get('cName', None)
# if disp:
#     manager.scan_and_save(ecom_provider='Dutchie', store="Due North Cannabis",
#                           shop_address="150 CHURCHILL BLVD UNIT C001", state="SAULT STE. MARIE",
#                           status="Authorized to Open",
#                           url="http://duenorthcannabis.com/", index=71, despensary_id=disp,
#                           service_options="['Curbside pickup', 'Delivery', 'In-store pickup', 'In-store shopping', 'Same-day delivery']")
# 60806bc5ece0aa00d28bff8d
