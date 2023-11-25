from typing import Union
import logging
import random

from selenium_stealth import stealth
from selenium.webdriver import Chrome
from seleniumwire.webdriver import Chrome as WireChrome
from seleniumwire.webdriver import ChromeOptions as WireChromeOptions

from base_selenium_worker import BaseSeleniumWorker


class WireWorker(BaseSeleniumWorker):
    @staticmethod
    def _create_wire_driver(
        options_args: Union[dict, None] = None,
        sw_options_args: dict = dict
    ) -> Chrome:
        selenium_logger = logging.getLogger('seleniumwire')
        selenium_logger.setLevel(logging.ERROR)
        sw_options = {
            'mitm_http2': False,
        }
        options = WireChromeOptions()
        if options_args:
            if options_args.get('options'):
                for arg in options_args['options'].keys():
                    options.add_argument(
                        f'{arg}={options_args["options"][arg]}')
            if options_args.get('experiment_options'):
                for arg in options_args['options'].keys():
                    options.add_experimental_option(
                        arg, options_args["experiment_options"][arg])
        for arg in sw_options_args.keys():
            sw_options[arg] = sw_options_args[arg]
        options.add_argument('--window-size=1920,1080')
        options.add_argument('--lang=en-US')
        driver = WireChrome(options=options, seleniumwire_options=sw_options)
        return driver

    @staticmethod
    def _create_wire_stealth_driver(
        options_args: Union[dict, None] = None,
        sw_options_args: dict = dict
    ) -> WireChrome:
        driver = WireWorker._create_wire_driver(
            options_args, sw_options_args)
        stealth(driver,
                languages=["en-US", "en"],
                vendor="Google Inc.",
                platform="Win32",
                webgl_vendor="Intel Inc.",
                renderer="Intel Iris OpenGL Engine",
                fix_hairline=True,
                )
        return driver

    @staticmethod
    def _create_wire_stealth_random_proxy_driver(
        idx: int = 2460,
        options_args: Union[dict, None] = None,
        sw_options_args: dict = {}
    ) -> WireChrome:
        proxy = f"127.0.0.1:{24000+random.randint(0, idx)}"
        sw_options_args['mitm_http2'] = False
        sw_options_args['proxy'] = {
                'http': f'http://{proxy}',
                'https': f'https://{proxy}'
        }
        driver = WireWorker._create_wire_stealth_driver(
            options_args, sw_options_args)
        return driver

    @staticmethod
    def _create_wire_stealth_proxy_driver(
        idx: int,
        options_args: Union[dict, None] = None,
        sw_options_args: dict = {}
    ) -> WireChrome:
        proxy = f"127.0.0.1:{24000+idx}"
        sw_options_args['mitm_http2'] = False
        sw_options_args['proxy'] = {
                'http': f'http://{proxy}',
                'https': f'https://{proxy}'
        }
        driver = WireWorker._create_wire_stealth_driver(
            options_args, sw_options_args)
        return driver
