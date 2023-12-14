from selenium.webdriver.common.by import By
from handy_wrappers import HandyWrapper
from selenium import webdriver


class Element_present_check:
    def run_test(self):
        base_url = "https://www.letskodeit.com/practice"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(10)
        hw = HandyWrapper(driver)
        driver.get(base_url)

        element_result1 = hw.is_element_present("name1", By.ID)
        print(element_result1)

        element_result2 = hw.is_element_present("//input[@id='name']", By.XPATH)
        print(element_result2)

        driver.quit()


checker = Element_present_check()
checker.run_test()
