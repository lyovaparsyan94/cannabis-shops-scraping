import time
from selenium import webdriver
from selenium.common.exceptions import *
from selenium.webdriver import ActionChains

from handy_wrappers import HandyWrapper
from selenium.webdriver.common.by import By
from explisit_wait_type import ExplicitWaitType
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service as Service
from selenium.webdriver.support import expected_conditions as EC
from platform_scrapper.configs.constants import *

url = "https://rate.am/"
service = Service()
driver = webdriver.Chrome(service=service)
driver.maximize_window()
driver.get(url)
els = driver.find_elements(By.CSS_SELECTOR, 'td.bank')
for el in els:
    ActionChains(driver).scroll_to_element(el).perform()
iframe = driver.find_element(By.CSS_SELECTOR, "#aspnetForm > div.footer")
ActionChains(driver).scroll_to_element(iframe).perform()
time.sleep(5)
driver.close()

















