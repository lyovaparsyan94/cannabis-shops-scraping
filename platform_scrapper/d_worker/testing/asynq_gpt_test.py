from gevent import monkey
import pprint
monkey.patch_all()
import gevent
import time
import requests

url = 'https://www.list.am/ru/category/'


def worker(url):
    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"}
        req = requests.get(url, headers=headers)
        content = req.content
        print(f"Content for {url}: {content[:50]}")
        res.append(url)
    except Exception as e:
        print(f"Error fetching {url}: {e}")

res = []

s = time.time()
jobs = [gevent.spawn(worker, f"{url}{i}") for i in range(300)]
gevent.joinall(jobs)
e = time.time()
print(f'time - {e - s}')
res = list(set(res))
pprint.pprint(res)
print(len(res))