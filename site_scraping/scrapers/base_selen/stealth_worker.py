from typing import Union
import random

from selenium_stealth import stealth
from selenium.webdriver import Chrome
from base_selenium_worker import BaseSeleniumWorker


class StealthWorker(BaseSeleniumWorker):

    __stealth_options = {
        "experiment_options": {
            "excludeSwitches": ["enable-automation"],
            'useAutomationExtension': False
        }
    }

    @staticmethod
    def _create_stealth_driver(options_args: dict = dict) -> Chrome:
        opts = StealthWorker.__stealth_options.copy()

        if options_args:
            if opts.get("experiment_options"):
                opts["experiment_options"] = options_args
            if opts.get("options"):
                opts["options"] = options_args
        driver = StealthWorker._create_driver(opts)
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
    def _create_random_proxy_stealth_driver(
        idx: int = 2460,
        options_args: Union[dict, None] = None
    ) -> Chrome:
        proxy = f"127.0.0.1:{24000+random.randint(0, idx)}"
        opts = {"options": {}, "experiment_options": {}}
        if options_args.get("options"):
            opts["options"] = options_args.get("options")
        if options_args.get("experiment_options"):
            opts["experiment_options"] = options_args.get("experiment_options")

        opts["options"] = {
                '--proxy-server': proxy,
            }

        driver = StealthWorker._create_stealth_driver(opts)
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
    def _create_proxy_stealth_driver(
        idx: int,
        options_args: Union[dict, None] = None
    ) -> Chrome:
        proxy = f"127.0.0.1:{24000+idx}"
        opts = {"options": {}, "experiment_options": {}}
        if options_args.get("options"):
            opts["options"] = options_args.get("options")
        if options_args.get("experiment_options"):
            opts["experiment_options"] = options_args.get("experiment_options")

        opts["options"] = {
                '--proxy-server': proxy,
            }

        driver = StealthWorker._create_stealth_driver(opts)
        stealth(driver,
                languages=["en-US", "en"],
                vendor="Google Inc.",
                platform="Win32",
                webgl_vendor="Intel Inc.",
                renderer="Intel Iris OpenGL Engine",
                fix_hairline=True,
                )
        return driver
