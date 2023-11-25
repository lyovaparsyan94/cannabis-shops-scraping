import random
from typing import Union

from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.action_chains import ActionChains


class BaseSeleniumWorker:
    def __init__(self) -> None:
        pass

    @staticmethod
    def _create_driver(options_args: Union[dict, None] = None) -> Chrome:
        options = Options()
        if options_args:
            if options_args.get('options'):
                for arg in options_args['options'].keys():
                    options.add_argument(
                        f'{arg}={options_args["options"][arg]}')
            if options_args.get('experiment_options'):
                for arg in options_args['options'].keys():
                    options.add_experimental_option(
                        arg, options_args["experiment_options"][arg])
        options.add_argument('--window-size=1920,1080')
        options.add_argument('--lang=en-US')
        driver = Chrome(options=options)
        driver.maximize_window()
        return driver

    @staticmethod
    def _create_random_proxy_driver(idx: int = 2460, options_args: Union[dict, None] = None) -> Chrome:
        opts = {"options": {}, "experiment_options": {}}
        if options_args.get("options"):
            opts["options"] = options_args.get("options")
        if options_args.get("experiment_options"):
            opts["experiment_options"] = options_args.get("experiment_options")
        proxy = f"127.0.0.1:{24000+random.randint(0, idx)}"
        opts["options"] = {
                '--proxy-server': proxy,
            }
        driver = BaseSeleniumWorker._create_driver(opts)
        return driver

    @staticmethod
    def _create_proxy_driver(idx: int, options_args: Union[dict, None] = None) -> Chrome:
        opts = {"options": {}, "experiment_options": {}}
        if options_args.get("options"):
            opts["options"] = options_args.get("options")
        if options_args.get("experiment_options"):
            opts["experiment_options"] = options_args.get("experiment_options")
        proxy = f"127.0.0.1:{24000+idx}"
        opts["options"] = {
                '--proxy-server': proxy,
            }
        driver = BaseSeleniumWorker._create_driver(opts)
        return driver

    @staticmethod
    def _jsclick(driver: Chrome, elem: WebElement) -> None:
        driver.execute_script('arguments[0].click();', elem)

    @staticmethod
    def _smooth_scroll(driver: Chrome, elem: WebElement):
        driver.execute_script(
            """arguments[0].scrollIntoView({block: "center", behavior: "smooth"});""", elem
        )

    @staticmethod
    def _action_click(driver: Chrome, elem: WebElement) -> None:
        action_chains = ActionChains(driver)
        action_chains.move_to_element(elem).click().perform()

    @staticmethod
    def _action_fill_input(driver: Chrome, elem: WebElement, text: str) -> None:
        action_chains = ActionChains(driver)
        action_chains.move_to_element(elem).click().send_keys(text).perform()
