import json
import time
import pandas as pd
from bs4 import BeautifulSoup
from urllib.parse import urlparse
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from configs.constants import BUDDI, DUTCHIE, TECHPOS, TYMBER, buddi_markers, dutchie_markers, techpos_markers, \
    tymber_markers


def start():
    try:
        counter = 1
        df = load_xlsx(
            r'/data/fake_cannabis_used_IDs.xlsx')
        for _, row in df.iterrows():
            store = row.iloc[1]
            url = row.iloc[4]
            current_data = current_info()
            data = current_data  # !!!! ES DZI
            print(f"Trying URL: {url}\n {counter}/{len(df)}")
            if url not in data and "cannacabana.com" not in url and counter > 224:
                if not current_data.get(urlparse(url).netloc, False):
                    scrape(store=store, url=url)
                else:
                    print(f"Current store {store} with {url} already in  saved data")
                    continue
            counter += 1
    except Exception as e:
        print(e)
        print("Can't continue, saving current data")
    finally:
        save_dict()


def scrape(store, url):
    try:
        driver.get(url)
        domain = urlparse(url).netloc
        time.sleep(5)
        print('Finding <a> tags')
        a_web_elements = driver.find_elements(*(By.TAG_NAME, 'a'))
        links = set([tag.get_attribute('href') for tag in a_web_elements])
        print(f'"a" tags founded: {links}')
        data[url] = {'store': store, 'src': None, 'platform': None}
        print('Length of data - ', len(data))
        for link in links:
            try:
                if domain in link:
                    print(f'Getting link {link}')
                    driver.get(link)
                    time.sleep(5)
                    soup = BeautifulSoup(driver.page_source, 'html.parser')
                    element = soup.select('#dutchie--embed__script')
                    if element:
                        src = element[0].get('src', None)
                        if src:
                            print(f'src founded: {src}')
                            data[url]['src'] = src
                            data[url]['platform'] = DUTCHIE
                            return
                    if not data[url].get('platform', None):
                        if is_platform(name=DUTCHIE, url=url, markers=dutchie_markers):
                            data[url]['platform'] = DUTCHIE
                        elif is_platform(name=BUDDI, url=url, markers=buddi_markers):
                            data[url]['platform'] = BUDDI
                        elif is_platform(name=TECHPOS, url=url, markers=techpos_markers):
                            data[url]['platform'] = TECHPOS
                        elif is_platform(name=TYMBER, url=url, markers=tymber_markers):
                            data[url]['platform'] = TYMBER
            except Exception as e:
                print(e)
                print(f'Store: {store}\nURL: {url}\n{100 * "="}')
    except Exception:
        print('Other exception')


def is_platform(name, url, markers):
    for marker in markers:
        if marker in driver.page_source:
            print(f"Found --{name}-- platform marker at {url}")
            return True
    else:
        print(f"{name} platform marker was not found at {url}")
        return False


def save_dict():
    with open('../data/info_save.json',
              'w') as f:
        json.dump(data, f)


def current_info():
    with open('data/info_save.json', "r") as file:
        file = json.load(file)
        return file


def load_xlsx(file):
    return pd.read_excel(file)


data = {}
service = Service(executable_path=r'..\DOT\drivers\chromedriver.exe')
driver = Chrome(service=service)
start()
