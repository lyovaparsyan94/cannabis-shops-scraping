import sys
import ssl


def serp_search(q: str):
    ssl._create_default_https_context = ssl._create_unverified_context
    if sys.version_info[0] == 2:
        import six
        from six.moves.urllib import request
        opener = request.build_opener(
            request.ProxyHandler(
                {'http': 'http://brd-customer-hl_4da8aa53-zone-serp:ex10mfl9n3l0@brd.superproxy.io:22225',
                 'https': 'http://brd-customer-hl_4da8aa53-zone-serp:ex10mfl9n3l0@brd.superproxy.io:22225'}))
        print(opener.open(f'http://www.google.com/search?q={q}').read())
    if sys.version_info[0] == 3:
        import urllib.request
        opener = urllib.request.build_opener(
            urllib.request.ProxyHandler(
                {'http': 'http://brd-customer-hl_4da8aa53-zone-serp:ex10mfl9n3l0@brd.superproxy.io:22225',
                 'https': 'http://brd-customer-hl_4da8aa53-zone-serp:ex10mfl9n3l0@brd.superproxy.io:22225'}))
        print(opener.open(f'http://www.google.com/search?q={q}').read())
