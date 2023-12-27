from gevent import monkey
# monkey.patch_all()
import json
import pprint
import time
import gevent
import requests
from data_collector import write_report
from platform_scrapper.configs.constants import HEADERS, consumer_headers
from scan_delivery_zone import ScanDutchieDelivery
from platform_scrapper.helpers.file_handler import load_xlsx


class Manager:
    def __init__(self):
        # self.scanner = ScanDutchieDelivery()
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
        print(f"SRC {src_id} response  {response.status_code}")
        if response.status_code == 200:
            if response.json()['data']['filteredDispensaries']:
                res = response.json()['data']['filteredDispensaries'][0]
                address = res['address']
                print(address)
                delivery_hours = res['deliveryHours']['Monday']['active']
                delivery_enabled = res['orderTypesConfig']['delivery']['enabled']
                url_with_endpoint = res['embeddedMenuUrl']
                cName = res['cName']
                print(f"got ---- cName {cName}")
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
                return query
            else:
                return None
        print(response.status_code, 'with', src_id)
        return None

    def start(self):
        df = load_xlsx(
            # file=r"C:\Users\1\OneDrive\Рабочий стол\DOT\cannabis-shops-scraping\platform_scrapper\src\test_cannabis_previous_for_apis.xlsx"
            file=r"C:\Users\1\OneDrive\Рабочий стол\DOT\cannabis-shops-scraping\platform_scrapper\src\1FAKECOPY_test_cannabis_previous_for_apis.xlsx"
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
            file=r"C:\Users\1\OneDrive\Рабочий стол\DOT\cannabis-shops-scraping\platform_scrapper\src\1FAKECOPY_test_cannabis_previous_for_apis.xlsx"
        )
        copy_df = df.fillna('', inplace=False)
        try:
            for index, row in copy_df.iterrows():
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
                ended_licension = "Public Notice Period: Ended"
                if store_id and len(store_id) == 24:
                    if ended_licension.lower() not in status.lower():
                        print(f"Licenzion is {ended_licension.lower() not in status.lower()}")
                        print(f"Trying to get query ... {index}, platform {ecom_provider}")
                    query = self.query_maker(src_id=store_id)
                    print(f"query is {query} for {store} {address}, url - {url} and store_id - {store_id}")
                    if query and query.get('delivery_enabled', None):
                        ln1 = query.get('ln1', None)
                        despensary_id = query.get('cName', None)
                        if ln1 and despensary_id:
                            print(f"getting coordinates: ln1 - {ln1}")
                            print(f"Preparing for scanning {store} {address} with {store}")
                            self.scanner = ScanDutchieDelivery(shop_address=ln1, despensary_id=despensary_id)
                            time.sleep(5)
                            global_data = {
                                "5.0": {
                                    "0": {
                                        "4.699999999999999": [
                                            [
                                                43.45168773119106,
                                                -79.8432439
                                            ],
                                            "min order - 50.0"
                                        ]
                                    },
                                    "10": {
                                        "4.699999999999999": [
                                            [
                                                43.45026487370072,
                                                -79.82094379617504
                                            ],
                                            "min order - 50.0"
                                        ]
                                    },
                                    "20": {
                                        "4.699999999999999": [
                                            [
                                                43.44603959903164,
                                                -79.79932331788973
                                            ],
                                            "min order - 50.0"
                                        ]
                                    },
                                    "30": {
                                        "4.699999999999999": [
                                            [
                                                43.43914047710801,
                                                -79.77904119233023
                                            ],
                                            "min order - 50.0"
                                        ]
                                    },
                                    "40": {
                                        "4.699999999999999": [
                                            [
                                                43.42977742071154,
                                                -79.76071501523997
                                            ],
                                            "min order - 50.0"
                                        ]
                                    },
                                    "50": {
                                        "4.699999999999999": [
                                            [
                                                43.418235272610865,
                                                -79.7449023244032
                                            ],
                                            "min order - 50.0"
                                        ]
                                    },
                                    "60": {
                                        "4.699999999999999": [
                                            [
                                                43.40486510819147,
                                                -79.73208357430255
                                            ],
                                            "min order - 50.0"
                                        ]
                                    },
                                    "70": {
                                        "4.699999999999999": [
                                            [
                                                43.39007352304656,
                                                -79.7226475393987
                                            ],
                                            "min order - 50.0"
                                        ]
                                    },
                                    "80": {
                                        "4.699999999999999": [
                                            [
                                                43.37431023651128,
                                                -79.71687958910331
                                            ],
                                            "min order - 50.0"
                                        ]
                                    },
                                    "90": {
                                        "4.699999999999999": [
                                            [
                                                43.3580543929145,
                                                -79.71495317979559
                                            ],
                                            "min order - 50.0"
                                        ]
                                    },
                                    "100": {
                                        "3.3": [
                                            [
                                                43.34916031350601,
                                                -79.77400628800393
                                            ],
                                            "min order - 50.0"
                                        ]
                                    },
                                    "110": {
                                        "3.3": [
                                            [
                                                43.34052277916381,
                                                -79.7771849493928
                                            ],
                                            "min order - 50.0"
                                        ]
                                    },
                                    "120": {
                                        "3.3": [
                                            [
                                                43.33241885662314,
                                                -79.78236952803427
                                            ],
                                            "min order - 50.0"
                                        ]
                                    },
                                    "130": {
                                        "3.3": [
                                            [
                                                43.32509466437931,
                                                -79.7894020609542
                                            ],
                                            "min order - 50.0"
                                        ]
                                    },
                                    "140": {
                                        "3.3": [
                                            [
                                                43.318772603332576,
                                                -79.79806863898136
                                            ],
                                            "min order - 50.0"
                                        ]
                                    },
                                    "150": {
                                        "3.3": [
                                            [
                                                43.31364461623945,
                                                -79.80810593368385
                                            ],
                                            "min order - 50.0"
                                        ]
                                    },
                                    "160": {
                                        "3.3": [
                                            [
                                                43.3098663736685,
                                                -79.81920919816095
                                            ],
                                            "min order - 50.0"
                                        ]
                                    },
                                    "170": {
                                        "3.3": [
                                            [
                                                43.307552560951976,
                                                -79.83104149867326
                                            ],
                                            "min order - 50.0"
                                        ]
                                    },
                                    "180": {
                                        "3.3": [
                                            [
                                                43.30677340730886,
                                                -79.8432439
                                            ],
                                            "min order - 50.0"
                                        ]
                                    },
                                    "190": {
                                        "3.3": [
                                            [
                                                43.307552560951976,
                                                -79.85544630132675
                                            ],
                                            "min order - 50.0"
                                        ]
                                    },
                                    "200": {
                                        "3.3": [
                                            [
                                                43.3098663736685,
                                                -79.86727860183906
                                            ],
                                            "min order - 50.0"
                                        ]
                                    },
                                    "210": {
                                        "3.3": [
                                            [
                                                43.31364461623945,
                                                -79.87838186631616
                                            ],
                                            "min order - 50.0"
                                        ]
                                    },
                                    "220": {
                                        "3.3": [
                                            [
                                                43.318772603332576,
                                                -79.88841916101865
                                            ],
                                            "min order - 50.0"
                                        ]
                                    },
                                    "230": {
                                        "3.3": [
                                            [
                                                43.32509466437931,
                                                -79.8970857390458
                                            ],
                                            "min order - 50.0"
                                        ]
                                    },
                                    "240": {
                                        "3.3": [
                                            [
                                                43.33241885662314,
                                                -79.90411827196574
                                            ],
                                            "min order - 50.0"
                                        ]
                                    },
                                    "250": {
                                        "3.3": [
                                            [
                                                43.34052277916381,
                                                -79.9093028506072
                                            ],
                                            "min order - 50.0"
                                        ]
                                    },
                                    "260": {
                                        "3.3": [
                                            [
                                                43.34916031350601,
                                                -79.91248151199608
                                            ],
                                            "min order - 50.0"
                                        ]
                                    },
                                    "270": {
                                        "4.699999999999999": [
                                            [
                                                43.3580543929145,
                                                -79.97153462020442
                                            ],
                                            "min order - 50.0"
                                        ]
                                    },
                                    "280": {
                                        "4.699999999999999": [
                                            [
                                                43.37431023651128,
                                                -79.9696082108967
                                            ],
                                            "min order - 50.0"
                                        ]
                                    },
                                    "290": {
                                        "4.699999999999999": [
                                            [
                                                43.39007352304656,
                                                -79.96384026060132
                                            ],
                                            "min order - 50.0"
                                        ]
                                    },
                                    "300": {
                                        "4.699999999999999": [
                                            [
                                                43.40486510819147,
                                                -79.95440422569746
                                            ],
                                            "min order - 50.0"
                                        ]
                                    },
                                    "310": {
                                        "4.699999999999999": [
                                            [
                                                43.418235272610865,
                                                -79.94158547559681
                                            ],
                                            "min order - 50.0"
                                        ]
                                    },
                                    "320": {
                                        "4.699999999999999": [
                                            [
                                                43.42977742071154,
                                                -79.92577278476004
                                            ],
                                            "min order - 50.0"
                                        ]
                                    },
                                    "330": {
                                        "4.699999999999999": [
                                            [
                                                43.43914047710801,
                                                -79.90744660766978
                                            ],
                                            "min order - 50.0"
                                        ]
                                    },
                                    "340": {
                                        "3.3": [
                                            [
                                                43.40628872274739,
                                                -79.86730628558918
                                            ],
                                            "min order - 50.0"
                                        ]
                                    },
                                    "350": {
                                        "3.3": [
                                            [
                                                43.40860419921312,
                                                -79.85546103154451
                                            ],
                                            "min order - 50.0"
                                        ]
                                    },
                                    "360": {
                                        "4.699999999999999": [
                                            [
                                                43.45168773119106,
                                                -79.8432439
                                            ],
                                            "min order - 50.0"
                                        ]
                                    }
                                }
                            }
                            global_data = self.scanner.multi_scan_total_area(store=store, address=address)
                            write_report(global_data=global_data, store=store, address=address, status=status, url=url,
                                         ecom_provider=ecom_provider, service_options=service_options, index=index)

                            raise Exception
                    else:
                        continue
        except Exception as e:
            print(e)
        finally:
            copy_df.to_excel(
                r'C:\Users\1\OneDrive\Рабочий стол\DOT\cannabis-shops-scraping\platform_scrapper\src\2FAKECOPY_test_cannabis_previous_for_apis.xlsx',
                index=False)


manager = Manager()
# manager.start()
manager.manage()
