from platform_scrapper.utilities.manager import Manager
manager = Manager()
disp = manager.query_maker('6036a8ea63cfbf00ea95af43').get('cName', None)
# if disp:
#     manager.scan_and_save(ecom_provider='Dutchie', store="Due North Cannabis",
#                           shop_address="150 CHURCHILL BLVD UNIT C001", state="SAULT STE. MARIE",
#                           status="Authorized to Open",
#                           url="http://duenorthcannabis.com/", index=71, despensary_id=disp,
#                           service_options="['Curbside pickup', 'Delivery', 'In-store pickup', 'In-store shopping', 'Same-day delivery']")
# BRAMPTON	Bodega Boyz	69 BRAMALEA RD SUITE 3	Authorized to Open	http://www.bodegaboyz.ca/	Dutchie	61d38e4ca8388a008cb50d87	['In-store shopping']	19054580439	['Delivery']
