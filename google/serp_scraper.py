import json
import os
import sys
import ssl
from urllib.error import HTTPError
from urllib.parse import quote

from dotenv import load_dotenv

from google.models import WeedShop


def serp_search(url: str, bd_auth: str):
    ssl._create_default_https_context = ssl._create_unverified_context
    if sys.version_info[0] == 2:
        import six
        from six.moves.urllib import request
        opener = request.build_opener(request.ProxyHandler({'http': f'http://{bd_auth}@brd.superproxy.io:22225','https': f'http://{bd_auth}@brd.superproxy.io:22225'}))
        page_data = opener.open(url).read()
    if sys.version_info[0] == 3:
        import urllib.request
        opener = urllib.request.build_opener(
            urllib.request.ProxyHandler(
                {'http': f'http://{bd_auth}@brd.superproxy.io:22225',
                 'https': f'http://{bd_auth}@brd.superproxy.io:22225'}))
        page_data = opener.open(url).read()
    return find_shop_url_in_google_result(page_data)


def find_shop_url_in_google_result(res: str):
    res_json = json.loads(res)
    link = None
    phone = None
    latitude = None
    longitude = None
    map_link = None
    options_list = []
    deliveries = []
    if res_json.get('organic'):
        organic = res_json.get('organic')[0]
        link = organic.get('link')
        phone = organic.get('phone')
        latitude = organic.get("latitude")
        longitude = organic.get("longitude")
        map_link = organic.get("map_link")
        tags = organic.get('tags')
        if tags:
            for tag in tags:
                if tag.get("group_id") == 'service_options':
                    service = tag.get('value_title_short')
                    options_list.append(service)
                    if 'delivery' in service.lower():
                        deliveries.append(service)
    return link, phone, options_list, latitude, longitude, map_link, deliveries


def find_all_shop_urls():
    load_dotenv()
    bd_login = os.environ.get('BD_LOGIN')
    bd_pwd = os.environ.get('BD_PWD')
    bd_auth = f'{bd_login}:{bd_pwd}'
    shops = WeedShop.objects.filter(store_url__isnull=True)
    length = len(shops)
    for idx, shop in enumerate(shops):
        if str(shop.address) in str(shop.store_name):
            q = shop.store_name
        else:
            q = f"{shop.store_name} {shop.address}"
        print(f'[{idx+1}/{length}] | {q}')
        url_q = quote(q)
        url = 'https://www.google.com/maps/search/' + url_q + '/?gl=us&hl=en&lum_json=1'
        for _ in range(5):
            try:
                store_url, phone, service_options, latitude, longitude, map_link, deliveries = serp_search(url, bd_auth)
                break
            except HTTPError as herr:
                print(f'[{idx+1}/{length}] [{_+1}/5] serp search failed with error: {herr}')
        else:
            raise Exception(f'[{idx+1}/{length}] serp search all attempts failed')
        msg = f'[{idx+1}/{length}] | {store_url=}; {phone=}; '\
              f'{latitude=}; {longitude=}; {map_link=}; {service_options=}; {deliveries=}'
        print(msg)
        shop.store_url = store_url
        shop.phone_number = phone
        shop.service_options = service_options
        shop.latitude = latitude
        shop.longitude = longitude
        shop.map_link = map_link
        shop.type_of_delivery_offered = deliveries
        shop.save()
