from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement
from site_scraping.scrapers.base_selen.base_selenium_worker import BaseSeleniumWorker


class ShopBaseScraper(BaseSeleniumWorker):

    _ecommerce = {
        #  basically u can see logo in shoppin/order/checkout pages"
        'Dutchie': ['<style>   id="dutchie--embed__styles"', '<title> with text "dutchie"'],  # if dutchie will be 100% on the order page
        'buddi': 'div id=buddi-app',  # on shopping page +++
        # !

        # ? in footer
        'weedmaps': '<a rel="noreferrer noopener" href="https://weedmaps.com/dispensaries/cannaverse-scarborough" data-type="URL" data-id="https://weedmaps.com/dispensaries/cannaverse-scarborough" target="_blank">weedmaps.com</a>',

        'leafly': '',


        'waio': '?',
        'reachecomm': '?'
    }

    def main(self):
        url = 'https://budderscannabis.ca/'
        driver = self._create_driver()
        driver.get(url)

        self._agree_age(driver)
        # wait age agree elems
        self._filter_nav(driver)
        # find nav elem
        # in nav find all button/a
        # check nav elems text?

    def _agree_age(self, driver: Chrome):
        pass

    def _check_page(self, driver: Chrome):
        pass

    def _filter_nav(self, driver: Chrome):
        navbar = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.TAG_NAME, "nav")))  # or header
        a_elems = navbar.find_elements(By.TAG_NAME, 'a')
        for a_elem in a_elems:
            if '' in a_elem.text:
                pass
        button_elems = navbar.find_elements(By.TAG_NAME, 'button')
        for button_elem in button_elems:
            if '' in button_elem.text:
                pass
        # check all nav links and check elems
            # if elem style 'id="dutchie--embed__styles"' on page then = Dutchie

    def _dutchie_checker(driver: Chrome):
        pass
        # need to find in nav shop page
            # if style 'id="dutchie--embed__styles"' precense on page => return True


if __name__ == '__main__':
    ShopBaseScraper().main()
