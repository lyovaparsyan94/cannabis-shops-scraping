from gevent import monkey
monkey.patch_all()
import json
import gevent
import requests
from data_collector import write_report
from platform_scrapper.configs.constants import consumer_headers, ecommerse_providers
from scan_delivery_zone import ScanDutchieDelivery
from platform_scrapper.helpers.file_handler import load_xlsx
from platform_scrapper.utilities.file_modifier import reporter


class Manager:

    def load_src_data(self):
        json_with_src = r"C:\Users\parsy\OneDrive\Desktop\DOT\cannabis-shops-scraping\platform_scrapper\helpers\info_save.json"
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
                       '":"%s"}}&extensions={"persistedQuery":{"version":1,"sha256Hash":"c4d04949a6ec1adc37ab8c46098a5dda463366b2cb0e1d923829f38781b3eb30"}}' % src_id
        gevent.sleep(3)
        response = requests.get(url=consumer_url, headers=consumer_headers)
        if response.status_code == 200:
            if response.json()['data']['filteredDispensaries']:
                res = response.json()['data']['filteredDispensaries'][0]
                graphql_shop_id = res['id']
                special_hours = res.get("specialHours", None)
                name = res['name']
                address = res['address']
                print(address)
                delivery_hours = res['deliveryHours']['Monday']['active']
                delivery_enabled = res['orderTypesConfig']['delivery']['enabled']
                url_with_endpoint = res['embeddedMenuUrl']
                cName = res['cName']
                fee_tiers = res['feeTiers']
                city = res['location']['city']
                coordinates = res['location']['geometry']['coordinates']
                ln1 = res['location']['ln1']
                ln2 = str(res['location']['ln2'])
                state_short = res['location']['state']
                zipcode = res['location']['zipcode']
                offer_delivery = res["offerDelivery"]
                is_open_status = res['status']
                print("fee_tiers:", fee_tiers)
                print(
                    f"delivery_enabled - {delivery_enabled}, offer_delivery - {offer_delivery} is_open_status {is_open_status}")
                if not offer_delivery:
                    print(
                        f"Delivery info for {name} at address {ln1} NOT Found from Dutchie ecommerse provider's server \ state_short: {state_short}, zipcode: {zipcode}")
                query = {"address": address, "delivery_hours": delivery_hours, "delivery_enabled": delivery_enabled,
                         "url_with_endpoint": url_with_endpoint, "cName": cName, 'city': city,
                         "coordinates": coordinates, 'offer_delivery': offer_delivery,
                         "zipcode": zipcode, "is_open_status": is_open_status,
                         "graphql_shop_id": graphql_shop_id, "special_hours": special_hours,
                         "state_short": state_short, 'ln1': ln1, 'ln2': ln2, "fee_tiers": fee_tiers}
                return query
            else:
                return None
        return None

    def start(self):
        df = load_xlsx(
            file=r"C:\Users\parsy\OneDrive\Desktop\DOT\cannabis-shops-scraping\platform_scrapper\data\fake_cannabis_used_IDs.xlsx"
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
                    if info_saved[url].get("platform", None) and (ecom_provider not in ecommerse_providers):
                        print(f"ecom_provider is {ecom_provider}")
                        ecom_provider = info_saved[url]["platform"]
                        print(f"Filled {address} (url: {url}) {info_saved[url]['platform']} ecom_provider")
                        copy_df.at[index, 'ecommerce provider'] = str(ecom_provider)
                        print(f"ADD {counter} ECOMMERSE PROVIDERS")
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
                            except Exception as s:
                                print(s)
        except Exception as e:
            print(e)
        finally:
            copy_df.to_excel(
                r'C:\Users\parsy\OneDrive\Desktop\DOT\cannabis-shops-scraping\platform_scrapper\src\FAKECOPY_cannabis_used_IDs.xlsx',
                index=False)

    def manage(self, file):
        print(f'running file {file}')
        df = load_xlsx(file=file)
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
                phone = str(row.iloc[8])
                type_of_delivery_offered = row.iloc[9]
                min_delivery_fee = row.iloc[11]
                zones = row.iloc[12]
                checked = row.iloc[13]
                ended_licension = "Public Notice Period: Ended"
                if checked not in ['True', 'true', 'ИСТИНА', 1.0]:
                    if store_id and len(store_id) > 10:
                        try:
                            query = self.query_maker(src_id=store_id)
                            if query:
                                despensary_id = query.get('cName', None)
                                check_status = False
                                if despensary_id:
                                    special_hours = query.get('special_hours', '')
                                    if not query.get('delivery_enabled', None):
                                        write_report(
                                            global_data=f"Delivery info for {store} at address {address} NOT Found from {ecom_provider} ecommerse provider's server",
                                            store=store, address=address,
                                            status=status, url=url, ecom_provider=ecom_provider,
                                            service_options=service_options, phone=phone,
                                            index='', special_hours=special_hours)
                                        df.at[index, 'checked'] = True
                                        continue
                                    gevent.sleep(10)
                                    coordinates = query.get('coordinates')
                                    state_short = query.get('state_short', None)
                                    zipcode = query.get('zipcode', None)
                                    print(
                                        f"Store {store}, address: {address} {state}, licenzion - {status}, platform {ecom_provider},  url - {url}, store_id - {store_id}, index - {index}")
                                    self.scan_area(state=state_short, store=store, shop_address=address,
                                                   despensary_id=despensary_id, status=status, url=url,
                                                   ecom_provider=ecom_provider, service_options=service_options,
                                                   phone=phone,
                                                   index=index, coordinates=coordinates, special_hours=special_hours)
                                    check_status = True
                                df.at[index, 'checked'] = check_status
                                print(f"Saved checked -  {check_status} to excel")
                        except Exception as check_error:
                            df.at[index, 'checked'] = 'Error'
                            print(check_error)
                            print('Wrote Error to  excel!!!')
                        finally:
                            df.to_excel(file, index=False)
                    elif 'no' in type_of_delivery_offered.lower():
                        if 'page doesn' in ecom_provider.lower():
                            type_of_delivery_offered = type_of_delivery_offered.replace(" / Page doesn't exist",
                                                                                        '').replace(" / Page doesn’t exist", '')
                        if ecom_provider in ecommerse_providers:
                            is_provider_string = f"From {ecom_provider} ecommerse provider's server"
                        else:
                            is_provider_string = ""
                        write_report(
                            global_data=f"Delivery info for {store} at address {address} NOT Found {is_provider_string}: {type_of_delivery_offered[2:-2]}",
                            store=store, address=address,
                            status=status, url=url, ecom_provider=ecom_provider,
                            service_options=service_options, phone=phone,
                            index='')
                        df.at[index, 'checked'] = True
                    elif ecom_provider in ecommerse_providers and 'Delivery' in type_of_delivery_offered:
                        if ecom_provider == "Buddi":
                            buddi_params = {'radius': 25, 'fee': 5, 'minimum': 70}
                        self.scan_area(state=state, store=store, shop_address=address,
                                       despensary_id='', status=status, url=url,
                                       ecom_provider=ecom_provider, service_options=service_options,
                                       phone=phone,
                                       index=index, coordinates='', special_hours='', min_delivery_fee=min_delivery_fee, buddi_params=buddi_params)
                        reporter(store=store, address=address, auto=True)
                        df.at[index, 'checked'] = True
                        continue
        except Exception as e:
            print(e)
        finally:
            df.to_excel(file, index=False)

    def scan_area(self, store, shop_address, state, despensary_id, status, url, ecom_provider, service_options, phone,
                  index, coordinates, special_hours, min_delivery_fee, buddi_params=None):
        self.scanner = ScanDutchieDelivery(shop_address=shop_address, state=state, store=store,
                                           despensary_id=despensary_id, coordinates=coordinates, provider=ecom_provider, buddi_params=buddi_params)
        try:
            global_data = self.scanner.multi_scan_total_area(store=store, address=shop_address, provider=ecom_provider,
                                                             state=state, buddi_params=buddi_params)
            write_report(global_data=global_data[0], store=store, address=shop_address,
                         status=status, url=url, ecom_provider=ecom_provider, service_options=service_options,
                         phone=phone,
                         index='', special_hours=special_hours, min_delivery_fee=min_delivery_fee)
            # reporter(store=store, address=shop_address, del_mode=False, auto=True)
        except Exception as n:
            print(f"ERROR in saving {n}")

    @staticmethod
    def file_modifier():
        df = load_xlsx(
            file=r"C:\Users\parsy\OneDrive\Desktop\DOT\cannabis-shops-scraping\platform_scrapper\data"
                 r"\fake_cannabis_used_IDs.xlsx"
        )
        df = df.fillna('', inplace=False)
        for index, row in df.iterrows():
            store = str(row.iloc[1])
            address = str(row.iloc[2])
            try:
                reporter(store=store, address=address, del_mode=False, auto=False)
            except TypeError as er:
                print(f"error with {store} {address}\n", er)


manager = Manager()
manager.manage(file=r"C:\Users\parsy\OneDrive\Desktop\DOT\cannabis-shops-scraping\platform_scrapper\data"
                    r"\fake_cannabis_used_IDs.xlsx")
