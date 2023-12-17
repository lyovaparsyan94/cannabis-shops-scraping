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


class BuddiScrapper:
    def __init__(self):
        self.driver = self.__initiate_driver()
        self.hw = HandyWrapper(self.driver)
        self.waiter = ExplicitWaitType(self.driver)

    def __initiate_driver(self):
        service = Service()
        driver = webdriver.Chrome(service=service)
        driver.maximize_window()
        return driver

    def open_url(self, url, age_xpath_list=None):
        status_age_confirmed = False
        self.driver.get(url=url)
        try:
            self.confirm_age_by_click(current_url=url, xpathes=age_xpath_list)
            print("---------------confirmed age--1----------------------")
            status_age_confirmed = True
        except:
            if self.need_select():
                self.confirm_by_select(current_url=url, xpathes=age_select)
            time.sleep(5)
        print("No need_select")
        if status_age_confirmed:
            platform = self.check_platform(markers=go_to_shop_markers)
            # write platform name to xlsx
            shop_page = "https://4kcannabis.ca/product-menu/"
            self.driver.get(url=shop_page)
            self.go_to_shop_iframe(iframe_path=dutchie_iframe)

    def go_to_shop_iframe(self, iframe_path):
        # self.driver.execute_script("window.scrollBy(0, 1000);")
        dutchieframe = self.driver.find_element(By.ID, iframe_path)
        ActionChains(self.driver).scroll_to_element(dutchieframe).perform()
        self.driver.switch_to.frame(iframe_path)


    def check_platform(self, markers):
        print("checking platform...")
        hrefs = []
        for xpath in markers:
            element = self.waiter.wait_for_element(xpath, locator_type="xpath", timeout=4)
            # element = self.driver.find_element(By.XPATH, xpath)
            # element_is_present = self.hw.is_element_present(xpath, By.XPATH)
            a_tags = self.driver.find_elements(By.TAG_NAME, 'a')
            if element:
                hrefs += list(set([a.get_attribute('href') for a in a_tags if a.get_attribute('href').startswith("http")]))
                break
        hrefs = list(set(hrefs))
        for href in hrefs:
            if href is not None:
                self.driver.get(href)
                if self.is_platform(name=DUTCHIE, url=href, markers=dutchie_markers):
                    return DUTCHIE
                if self.is_platform(name=BUDDI, url=href, markers=buddi_markers):
                    return BUDDI
                if self.is_platform(name=LEAFLY, url=href, markers=leafly_markers):
                    return LEAFLY
                if self.is_platform(name=WEEDMAPS, url=href, markers=weedmaps_markers):
                    return WEEDMAPS

    def is_platform(self, name, url, markers):
        for marker in markers:
            if marker in self.driver.page_source:
                print(f"Found --{name}-- platform marker at {url}")
                return True
        else:
            print(f"{name} platform marker was not found at {url}")
            return False

    def need_select(self):
        need = False
        yes_option = "//select/option[contains(translate(text(), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), 'yes')]"
        no_option = "//select/option[contains(translate(text(), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), 'no')]"
        try:
            yes = self.waiter.wait_for_element(yes_option, locator_type="xpath", timeout=15)
            yes_is_present = self.hw.is_element_present(yes_option, By.XPATH)
            no_is_present = self.hw.is_element_present(no_option, By.XPATH)
            if yes_is_present:
                need = True
                return True
            if no_is_present:
                need = True
                return True
            print("No need to select")
        except Exception:
            print("can't decide need select or not")
            return need

    def confirm_age_by_click(self, current_url, xpathes):
        confirmed = False
        for xpth in xpathes:
            element = self.waiter.wait_for_element(xpth, locator_type="xpath", timeout=4)
            element_is_present = self.hw.is_element_present(xpth, By.XPATH)
            if element_is_present:
                print(f"element is displayed - {element.is_displayed()}")
                print(f"element is enabled -{element.is_enabled()}")
                try:
                    print(f"trying with xpath {xpth}")
                    element.click()
                    print(f"Age confirmed on {current_url}")
                    confirmed = True
                    return confirmed
                except NoSuchElementException:
                    print(f"No element with xpath {xpth}")
                    continue
            else:
                continue
        return confirmed

    def confirm_by_select(self, current_url, xpathes):
        confirmed = False
        for xpth in xpathes:
            element = self.driver.find_element(By.TAG_NAME, "select")
            element.click()
            element_is_present = self.hw.is_element_present(xpth, By.XPATH)
            if element_is_present:
                try:
                    yes = self.driver.find_element(By.XPATH, xpth)
                    yes.click()
                    print(f"Selected confirmed on")
                    confirm = self.driver.find_element(By.XPATH,
                                                       "//button[contains(translate(text(), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), 'age')]")
                    confirm.click()
                    confirmed = True
                    print(f"Age confirmed on {current_url}")
                    self.driver.refresh()
                    time.sleep(4)
                    return confirmed
                except NoSuchElementException:
                    print(f"No element with xpath {xpth}")
                    time.sleep(3)
                    continue
            else:
                continue
        return confirmed


worker = BuddiScrapper()
url = "https://4kcannabis.ca/"
# url = "https://bluebirdcannabis.store/"
# url = "http://dreamcannabis.net/"
# # url = "http://rcbudshop.ca/"
# # url = "http://twocatscannabisco.com/"
# # url = "http://www.discountedcannabis.ca/"
# # url = "http://www.shinybud.com/blenheim"
# # url = "http://www.smokelab.ca/"
# url = "https://missjonescannabis.com/"
worker.open_url(url, age_xpath_list=age_xpath_list)
