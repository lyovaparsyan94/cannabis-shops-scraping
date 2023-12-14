import time

from  selenium import webdriver
from selenium.webdriver.common.by import By

class Get_text:
    def run_test(self):
        base_url = "https://www.letskodeit.com/practice"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(base_url)
        open_tab_element = driver.find_element(By.ID, "opentab")
        text_of_tab_element = open_tab_element.text
        print(text_of_tab_element)
        time.sleep(2)
        driver.quit()

class Get_attribute:
    def run_test(self):
        base_url = "https://www.letskodeit.com/practice"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(base_url)

        el = driver.find_element(By.ID, "bmwcheck")
        result = el.get_attribute("value")
        print("value of attribute is: ", result)
        time.sleep(2)
        driver.quit()

worker = Get_text()
# worker.run_test()
worker1 = Get_attribute()
worker1.run_test()
