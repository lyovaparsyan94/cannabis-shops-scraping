from gevent import monkey
monkey.patch_all()
import json
import time
import gevent
import requests
from data_collector import write_report
from platform_scrapper.configs.constants import consumer_headers
from scan_delivery_zone import ScanDutchieDelivery
from platform_scrapper.helpers.file_handler import load_xlsx


class Manager:
    def __init__(self):
        ...

    def load_src_data(self):
        json_with_src = r"C:\Users\1\OneDrive\Рабочий стол\DOT\cannabis-shops-scraping\platform_scrapper\info_saved.json"
        with open(json_with_src, 'r') as file:
            data = json.load(file)
        return data

    def unparse_src(self, src_string):
        start = "https://dutchie.com/api/v2/embedded-menu/"
        end = ".js"
        src = src_string[len(start): -(len(end))]
        return src

    def query_maker(self, src_id=None):
        if src_id is not None:
            if len(src_id) > 24:
                src_id = self.unparse_src(src_string=src_id)
        else:
            return None
        consumer_url = 'https://dutchie.com/graphql?operationName=ConsumerDispensaries&variables={"dispensaryFilter":{"cNameOrID' \
                       '":"%s"}}&extensions={"persistedQuery":{"version":1,"sha256Hash":"4f415a7b945a5c58d2cf92ace12a3e24e40815' \
                       'f05f0755adc285d86f584d15c3"}}' % src_id
        gevent.sleep(3)
        response = requests.get(url=consumer_url, headers=consumer_headers)
        if response.status_code == 200:
            if response.json()['data']['filteredDispensaries']:
                res = response.json()['data']['filteredDispensaries'][0]
                address = res['address']
                delivery_hours = res['deliveryHours']['Monday']['active']
                delivery_enabled = res['orderTypesConfig']['delivery']['enabled']
                url_with_endpoint = res['embeddedMenuUrl']
                cName = res['cName']
                city = res['location']['city']
                coordinates = res['location']['geometry']['coordinates']
                ln1 = res['location']['ln1']
                ln2 = str(res['location']['ln2'])
                state_short = res['location']['state']
                zipcode = res['location']['zipcode']
                query = {"address": address, "delivery_hours": delivery_hours, "delivery_enabled": delivery_enabled,
                         "url_with_endpoint": url_with_endpoint, "cName": cName, 'city': city,
                         "coordinates": coordinates,
                         "zipcode": zipcode,
                         "state_short": state_short, 'ln1': ln1, 'ln2': ln2}
                print(f"Got query for {address}, ln1 - {ln1}, ln2: {ln2}")
                return query
            else:
                return None
        return None

    def start(self):
        df = load_xlsx(
            # file=r"C:\Users\1\OneDrive\Рабочий стол\DOT\cannabis-shops-scraping\platform_scrapper\src\test_cannabis_previous_for_apis.xlsx"
            file=r"C:\Users\1\OneDrive\Рабочий стол\DOT\cannabis-shops-scraping\platform_scrapper\src\3FAKECOPY_test_cannabis_previous_for_apis.xlsx"
        )
        copy_df = df.fillna('', inplace=False)

        info_saved = self.load_src_data()
        try:
            counter = 0
            for index, row in copy_df.iterrows():
                state = row.iloc[0]
                store = str(row.iloc[1])
                address = str(row.iloc[2])
                status = row.iloc[3]
                url = row.iloc[4]
                ecom_provider = row.iloc[5]
                store_id = row.iloc[6]
                service_options = row.iloc[7]
                phone = row.iloc[8]
                type_of_delivery_offered = row.iloc[9]
                delivery_qualifications = row.iloc[10]
                min_delivery_fee = row.iloc[11]
                zones = row.iloc[12]
                ended_licension = "Public Notice Period: Ended"

                if url in info_saved:
                    print(f"{url} in info_saved, index: {index}")
                    if info_saved[url].get("platform", None) and not ecom_provider:
                        ecom_provider = info_saved[url]["platform"]
                        copy_df.at[index, 'ecommerce provider'] = 'KK' + str(ecom_provider)
                        print(f"ADD {counter} ECOMMERSE PROVIDERS - ")
                        counter += 1

                    if str(info_saved[url]['store']).lower() in store.lower():
                        src = info_saved[url].get('src')
                        if src:
                            query = self.query_maker(src_id=src)
                            try:
                                if str(query.get('ln1', None).lower().split()[0]) in \
                                        address.lower().split()[0] or address.lower().split()[0] in \
                                        query.get('ln1', None).lower().split()[0]:
                                    print(f"NOT storeID {not store_id}")
                                    if not store_id:
                                        copy_df.at[index, 'ID'] = self.unparse_src(src)
                                        print(f"---added src to {address}")
                                    if query.get('delivery_enabled', None) is not None:
                                        print(f"Delivery types {query.get('delivery_enabled', None)}")
                                        if query.get('delivery_enabled', False):
                                            copy_df.at[index, 'type of delivery offered'] = ['Delivery',
                                                                                             'Same-day delivery']
                                            print("add delivery, same day")
                                        else:
                                            copy_df.at[index, 'type of delivery offered'] = ['No delivery']
                                    print("checking licenzion")
                                    if ended_licension.lower() not in status.lower():
                                        if store_id and len(store_id) == 24:
                                            print(f"Trying to get query ... {index}, platform {ecom_provider}")
                                        query = self.query_maker(src_id=store_id)
                                        print(f"query is for {store} {address} and store_id - {store_id}")
                                        if query and query.get('delivery_enabled', None):
                                            coordinates = query.get('coordinates', None)
                                            print(f"getting coordinates: {coordinates}")
                                            if coordinates:
                                                print(f"Preaparing for scanning {store} {address} with {store}")
                                                scannner = self.scanner.multi_scan_total_area(store=store,
                                                                                              address=coordinates)
                                                raise Exception
                                        else:
                                            continue

                            except Exception as s:
                                print(s)
                            finally:
                                continue
        except Exception as e:
            print(e)
        finally:
            copy_df.to_excel(
                r'C:\Users\1\OneDrive\Рабочий стол\DOT\cannabis-shops-scraping\platform_scrapper\src\2FAKECOPY_test_cannabis_previous_for_apis.xlsx',
                index=False)

    def manage(self):
        df = load_xlsx(
            file=r"C:\Users\1\OneDrive\Рабочий стол\DOT\cannabis-shops-scraping\platform_scrapper\src\3FAKECOPY_test_cannabis_previous_for_apis.xlsx"
        )
        df = df.fillna('', inplace=False)
        try:
            for index, row in df.iterrows():
                state = row.iloc[0]
                store = str(row.iloc[1])
                address = str(row.iloc[2])
                status = row.iloc[3]
                url = row.iloc[4]
                ecom_provider = row.iloc[5]
                store_id = row.iloc[6]
                service_options = row.iloc[7]
                type_of_delivery_offered = row.iloc[9]
                delivery_qualifications = row.iloc[10]
                min_delivery_fee = row.iloc[11]
                zones = row.iloc[12]
                checked = row.iloc[13]
                ended_licension = "Public Notice Period: Ended"
                if not checked and index > 172:
                    try:
                        if store_id and len(store_id) == 24:
                            if ended_licension.lower() not in status.lower():
                                print(f"Trying to get query {store} {address} {index}, platform {ecom_provider}")
                            query = self.query_maker(src_id=store_id)
                            if query:
                                ln1 = query.get('ln1', None)
                                despensary_id = query.get('cName', None)
                                if ln1 and despensary_id:
                                    time.sleep(10)
                                    print(
                                        f"Store{store} address: {address} {state}, check status - {checked}, licenzion - {status}, platform {ecom_provider},  url - {url}, and store_id - {store_id}, index - {index}")
                                    self.scan_and_save(state=state, store=store, shop_address=address, despensary_id=despensary_id, status=status, url=url, ecom_provider=ecom_provider, service_options=service_options,index=index)
                            else:
                                continue
                    except Exception as check_error:
                        df.at[index, 'checked'] = 'error with checking' + str(check_error)
                else:
                    continue
        except Exception as e:
            print(e)


    def scan_and_save(self,  store, shop_address, state, despensary_id, status, url, ecom_provider, service_options,
                      index):
        self.scanner = ScanDutchieDelivery(shop_address=shop_address, state=state,store=store, despensary_id=despensary_id)
        try:
            global_data = self.scanner.multi_scan_total_area(store=store,
                                                             address=shop_address)
            write_report(global_data=global_data[0], store=store, address=shop_address,
                         status=status,
                         url=url,
                         ecom_provider=ecom_provider, service_options=service_options,
                         index=index)
            print(f"Wrote {global_data[0]} file, removed json with same name and marked status to True, at index {index}")
            copy_df.at[index, 'checked'] = 'True'
        except Exception as n:
            print(f"ERROR in saving {n}")


copy_df = load_xlsx(
            file=r"C:\Users\1\OneDrive\Рабочий стол\DOT\cannabis-shops-scraping\platform_scrapper\src\3FAKECOPY_test_cannabis_previous_for_apis.xlsx")
manager = Manager()
# manager.start()
manager.manage()
# disp = manager.query_maker('5fd7995b81bf8a00d277da44').get('cName', None)
# if disp:
#     manager.scan_and_save(copy_df=copy_df, ecom_provider='Dutchie', store="The Peace Pipe", shop_address="31 CELINA ST", state="OSHAWA", status="Authorized to Open",
#                           url="http://peacepipe420.com/", index=3, despensary_id=disp, service_options="['Delivery', 'In-store pickup', 'In-store shopping']")