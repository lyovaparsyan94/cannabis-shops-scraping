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
        # find nav elem
        # in nav find all button/a
        # check nav elems text?


if __name__ == '__main__':
    ShopBaseScraper().main()
