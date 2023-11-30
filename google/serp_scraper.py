import json
import os
import sys
import ssl
from urllib.parse import quote

from dotenv import load_dotenv

from google.models import WeedShop


def serp_search(url: str, bd_auth: str):
    ssl._create_default_https_context = ssl._create_unverified_context
    if sys.version_info[0] == 2:
        import six
        from six.moves.urllib import request
        opener = request.build_opener(
            request.ProxyHandler(
                {'http': f'http://{bd_auth}@brd.superproxy.io:22225',
                 'https': f'http://{bd_auth}@brd.superproxy.io:22225'}))
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
                    options_list.append(tag.get('value_title_short'))

    return link, phone, options_list, latitude, longitude, map_link


def find_all_shop_urls():
    load_dotenv()
    bd_login = os.environ.get('BD_LOGIN')
    bd_pwd = os.environ.get('BD_PWD')
    bd_auth = f'{bd_login}:{bd_pwd}'
    shops = WeedShop.objects.filter(store_url__isnull=True)
    for idx, shop in enumerate(shops):
        q = f"{shop.store_name} {shop.address}"
        print(f'[{idx+1}/{len(shops)}] | {q}')
        # q = 'Hemisphere Cannabis Co. 700 King St W Unit #4, Toronto, ON M5V 2Y6'
        url_q = quote(q)
        url = 'https://www.google.com/maps/search/' + url_q + '/?gl=us&lum_json=1'
        store_url, phone, service_options, latitude, longitude, map_link = serp_search(url, bd_auth)
        print(f'[{idx+1}/{len(shops)}] | {store_url=}; {phone=}; {latitude=}; {longitude=}; {map_link=} {service_options=}')
        shop.store_url = store_url
        shop.phone_number = phone
        shop.service_options = service_options
        shop.latitude = latitude
        shop.longitude = longitude
        shop.map_link = map_link
        shop.save()
