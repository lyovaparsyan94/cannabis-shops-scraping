from platform_scrapper.utilities.manager import Manager


manager = Manager()
disp = manager.query_maker('60086c94f8526427d535d1d1').get('cName', None)
# if disp:
#     manager.scan_and_save(ecom_provider='Dutchie', store="Due North Cannabis",
#                           shop_address="150 CHURCHILL BLVD UNIT C001", state="SAULT STE. MARIE",
#                           status="Authorized to Open",
#                           url="http://duenorthcannabis.com/", index=71, despensary_id=disp,
#                           service_options="['Curbside pickup', 'Delivery', 'In-store pickup', 'In-store shopping', 'Same-day delivery']")
