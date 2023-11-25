import os
import sys
import ssl
from urllib.parse import quote

from bs4 import BeautifulSoup
from dotenv import load_dotenv

from google.models import WeedShop


def serp_search(q: str, bd_login: str, bd_pwd: str):
    ssl._create_default_https_context = ssl._create_unverified_context
    bd_auth = f'{bd_login}:{bd_pwd}'
    if sys.version_info[0] == 2:
        import six
        from six.moves.urllib import request
        opener = request.build_opener(
            request.ProxyHandler(
                {'http': f'http://{bd_auth}@brd.superproxy.io:22225',
                 'https': f'http://{bd_auth}@brd.superproxy.io:22225'}))
        page_data = opener.open(f'http://www.google.com/search?q={q}').read()
    if sys.version_info[0] == 3:
        import urllib.request
        opener = urllib.request.build_opener(
            urllib.request.ProxyHandler(
                {'http': f'http://{bd_auth}@brd.superproxy.io:22225',
                 'https': f'http://{bd_auth}@brd.superproxy.io:22225'}))
        page_data = opener.open(f'http://www.google.com/search?q={q}').read()
    return find_shop_url_in_google_result(page_data)


def find_shop_url_in_google_result(res):
    soup = BeautifulSoup(res, "lxml")
    rso_div = soup.find('div', {'id': 'rso'})
    url = rso_div.find_all('a')[0].get('href')
    return url


def find_all_shop_urls():
    load_dotenv()
    bd_login = os.environ.get('BD_LOGIN')
    bd_pwd = os.environ.get('BD_PWD')
    shops = WeedShop.objects.filter(store_url__isnull=True)
    for shop in shops:
        q = f'{shop.store_name} {shop.address}'
        url_q = quote(q)
        store_url = serp_search(url_q, bd_login, bd_pwd)
        shop.store_url = store_url
        shop.save()
