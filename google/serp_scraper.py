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
    if res_json.get('organic'):
        organic = res_json.get('organic')[0]
        link = organic.get('link')
    return link


def find_all_shop_urls():
    load_dotenv()
    bd_login = os.environ.get('BD_LOGIN')
    bd_pwd = os.environ.get('BD_PWD')
    bd_auth = f'{bd_login}:{bd_pwd}'
    shops = WeedShop.objects.filter(store_url__isnull=True)
    for shop in shops:
        q = f'{shop.store_name} {shop.address}'
        url_q = quote(q)
        url = 'https://www.google.com/maps/search/' + url_q + '/?gl=us&lum_json=1'
        store_url = serp_search(url, bd_auth)
        print(store_url)
        if store_url:
            shop.store_url = store_url
            shop.save()
