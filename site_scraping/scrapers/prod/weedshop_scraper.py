from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement

from site_scraping.scrapers.base_selen.base_selenium_worker import BaseSeleniumWorker


class ShopBaseScraper(BaseSeleniumWorker):
    contact_page_vars = [
        '/stores',
        '/contact-us/',
        '/pages/store-locator',
        '/contact/',
        '/#contact'
    ]
    order_page_vars = [
        '/order',
        '/product-menu/'
    ]

    delivery_page_vars = [
        ''
    ]

    def main(self):
        url = 'https://budderscannabis.ca/'
        driver = self._create_driver()
        driver.get(url)
        # wait age agree elems
        self._filter_nav(driver)
        # find nav elem
        # in nav find all button/a
        # check nav elems text?

    def _filter_nav(self, driver: Chrome):
        navbar = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.TAG_NAME, "nav")))
        a_elems = navbar.find_elements(By.TAG_NAME, 'a')
        for a_elem in a_elems:
            if '' in a_elem.text:
                pass
        button_elems = navbar.find_element(By.TAG_NAME, 'button')
        for button_elem in button_elems:
            if '' in button_elem.text:
                pass


if __name__ == '__main__':
    ShopBaseScraper().main()
