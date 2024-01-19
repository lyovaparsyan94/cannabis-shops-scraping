from handy_wrappers import HandyWrapper
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *


class ExplicitWaitType:

    def __init__(self, driver):
        self.driver = driver
        self.hw = HandyWrapper(driver=driver)

    def wait_for_element(self, locator, locator_type='id', timeout=10, poll_frequency=0.5):
        element = None
        try:
            self.driver.implicitly_wait(0)
            by_type = self.hw.get_by_type(locator_type)
            print(f"Waiting for maximum ---{str(timeout)} ---- seconds for element to be clickable")
            wait = WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll_frequency, ignored_exceptions=[
                NoSuchElementException,
                ElementNotVisibleException,
                ElementNotSelectableException])
            element = wait.until(EC.visibility_of_element_located((by_type, locator)))
            print(f"Element appeared on the web page with {locator}")
        except:
            print(f"Element NOT appeared on the web page {locator}")
            # print_stack()
            self.driver.implicitly_wait(2)
        return element


