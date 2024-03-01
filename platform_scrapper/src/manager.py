from gevent import monkey  # noqa:  E402
monkey.patch_all()  # noqa:  E402
import json
import gevent
import requests
from utilities.file_handler import load_xlsx
from utilities.file_modifier import reporter
from utilities.data_collector import write_report
from platform_scrapper.configs.file_constantns import FAKE_CANNABIS_USED
from platform_scrapper.src.scan_delivery_zone import ScanDutchieDelivery
from platform_scrapper.configs.constants import consumer_headers, ecommerse_providers, ended_licension, DUTCHIE


class Manager:

    @staticmethod
    def load_src_data():
        json_with_src = r"../data/info_save.json"
        with open(json_with_src, 'r') as file:
            data = json.load(file)
        return data

    @staticmethod
    def unparse_src(src_string):
        start = "https://dutchie.com/api/v2/embedded-menu/"
        end = ".js"
        src = src_string[len(start): -(len(end))]
        return src

    def query_maker(self, src_id=None):
        if src_id is not None:
            if len(src_id) > 26:
                src_id = self.unparse_src(src_string=src_id)
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
                # print("fee_tiers:", fee_tiers)
                print(
                    f"delivery_enabled - {delivery_enabled}, offer_delivery - {offer_delivery} is_open_status {is_open_status}")
                if not offer_delivery:
                    print(
                        f"Delivery info for {name} at address {ln1} NOT Found from Dutchie ecommerse provider's server : state_short: {state_short}, zipcode: {zipcode}")
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
        df = load_xlsx(file=FAKE_CANNABIS_USED)
        copy_df = df.fillna('', inplace=False)
        info_saved = self.load_src_data()
        try:
            counter = 0
            for index, row in copy_df.iterrows():
                store = str(row.iloc[1])
                address = str(row.iloc[2])
                status = row.iloc[3]
                url = row.iloc[4]
                ecom_provider = row.iloc[5]
                store_id = row.iloc[6]
                if url in info_saved:
                    if info_saved[url].get("platform", None) and (ecom_provider not in ecommerse_providers):
                        ecom_provider = info_saved[url]["platform"]
                        copy_df.at[index, 'ecommerce provider'] = str(ecom_provider)
                        counter += 1
                    if str(info_saved[url]['store']).lower() in store.lower():
                        src = info_saved[url].get('src')
                        if src:
                            query = self.query_maker(src_id=src)
                            try:
                                if str(query.get('ln1', None).lower().split()[0]) in \
                                        address.lower().split()[0] or address.lower().split()[0] in \
                                        query.get('ln1', None).lower().split()[0]:
                                    if not store_id:
                                        copy_df.at[index, 'ID'] = self.unparse_src(src)
                                        print(f"---added src to {address}")
                                    if query.get('delivery_enabled', None) is not None:
                                        print(f"Delivery types {query.get('delivery_enabled', None)}")
                                        if query.get('delivery_enabled', False):
                                            copy_df.at[index, 'type of delivery offered'] = ['Delivery',
                                                                                             'Same-day delivery']
                                        else:
                                            copy_df.at[index, 'type of delivery offered'] = ['No delivery']
                                    if ended_licension.lower() not in status.lower():
                                        if store_id and len(store_id) == 24:
                                            print(f"Trying to get query ... {index}, platform {ecom_provider}")
                                        query = self.query_maker(src_id=store_id)
                                        print(f"query is for {store} {address} and store_id - {store_id}")
                                        if query and query.get('delivery_enabled', None):
                                            coordinates = query.get('coordinates', None)
                                            print(f"getting coordinates: {coordinates}")
                                            if coordinates:
                                                scannner = self.scanner.multi_scan_total_area(store=store,
                                                                                              address=coordinates)
                                                raise Exception
                            except Exception as s:
                                print(s)
        except Exception as e:
            print(e)
        finally:
            copy_df.to_excel(FAKE_CANNABIS_USED, index=False)

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
                checked = row.iloc[13]
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
                                    print(
                                        f"Store {store}, address: {address} {state}, licenzion - {status}, platform {ecom_provider},  url - {url}, store_id - {store_id}, index - {index}")
                                    self.scan_area(state=state_short, store=store, shop_address=address,
                                                   despensary_id=despensary_id, status=status, url=url,
                                                   ecom_provider=ecom_provider, service_options=service_options,
                                                   phone=phone, min_delivery_fee=None,
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
                                                                                        '').replace(
                                " / Page doesn’t exist", '')
                        if ecom_provider in ecommerse_providers:
                            is_provider_string = f"From {ecom_provider} ecommerse provider's server"
                        else:
                            is_provider_string = ""
                        write_report(
                            global_data=f"Delivery info for {store} at address {address} NOT Found {is_provider_string}: {type_of_delivery_offered[2:-2]}",
                            store=store, address=address,
                            status=status, url=url, ecom_provider=ecom_provider,
                            service_options=service_options, phone=phone,
                            index='', special_hours='')
                        df.at[index, 'checked'] = True
                    elif ecom_provider in ecommerse_providers and 'Delivery' in type_of_delivery_offered:
                        if ecom_provider in ecommerse_providers and ecom_provider != DUTCHIE:
                            buddi_params = {'radius': 5, 'fee': 0, 'minimum': 9.95}
                        self.scan_area(state=state, store=store, shop_address=address,
                                       despensary_id='', status=status, url=url,
                                       ecom_provider=ecom_provider, service_options=service_options,
                                       phone=phone,
                                       index=index, coordinates='', special_hours='', min_delivery_fee=min_delivery_fee,
                                       buddi_params=buddi_params)
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
                                           despensary_id=despensary_id, coordinates=coordinates, provider=ecom_provider,
                                           buddi_params=buddi_params)
        try:
            global_data = self.scanner.multi_scan_total_area(store=store, address=shop_address, provider=ecom_provider,
                                                             buddi_params=buddi_params)
            write_report(global_data=global_data[0], store=store, address=shop_address,
                         status=status, url=url, ecom_provider=ecom_provider, service_options=service_options,
                         phone=phone,
                         index='', special_hours=special_hours, min_delivery_fee=min_delivery_fee)
        except Exception as n:
            print(f"ERROR in saving {n}")

    @staticmethod
    def file_modifier():
        df = load_xlsx(
            file=FAKE_CANNABIS_USED)
        df = df.fillna('', inplace=False)
        for _, row in df.iterrows():
            store = str(row.iloc[1])
            address = str(row.iloc[2])
            try:
                reporter(store=store, address=address, del_mode=False, auto=False)
            except TypeError as er:
                print(f"error with {store} {address}\n", er)
