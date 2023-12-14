import time
from selenium import webdriver
from selenium.common.exceptions import *
from handy_wrappers import HandyWrapper
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from explisit_wait_type import ExplicitWaitType
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service as Service
from selenium.webdriver.support import expected_conditions as EC
from platform_scrapper.configs.constants import weedmap_no_bot, age_xpath_list, age_select


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
        current_status_of_confirmation = False
        self.driver.get(url=url)
        self.driver.refresh()
        if not self.confirm_age_by_click(current_url=url, xpathes=age_xpath_list):
            print("---------------Tryed confirm by click----------------------")
        else:
            if self.need_select():
                self.confirm_by_select(current_url=url, xpathes=age_select)
            time.sleep(5)
        print("No need_select")

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
# url = "https://4kcannabis.ca/"
# url = "https://bluebirdcannabis.store/"
# url = "http://dreamcannabis.net/"
# url = "http://rcbudshop.ca/"
# url = "http://twocatscannabisco.com/"
# url = "http://www.discountedcannabis.ca/"
# url = "http://www.shinybud.com/blenheim"
# url = "http://www.smokelab.ca/"
url = "https://missjonescannabis.com/"
worker.open_url(url, age_xpath_list=age_xpath_list)
