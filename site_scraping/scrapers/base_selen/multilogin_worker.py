import json
import requests
from uuid import uuid4
from typing import Union

from selenium.webdriver import Remote
from selenium.webdriver.chrome.options import Options

from base_selenium_worker import BaseSeleniumWorker


class MultiloginWorker(BaseSeleniumWorker):

    def __init__(self, PORT=35100) -> None:
        self.PORT = PORT

    def _create_profile(self, proxy_port: Union[int, None] = None):
        """
        If proxy port provided - creating profile with proxy. If not - creating profile without proxy
        """
        url = f'http://localhost:{self.PORT}/api/v2/profile'
        if proxy_port:
            port = f'{24000+proxy_port}'
            body = {
                'name': f'bonga_{proxy_port}',
                'browser': 'mimic',
                'os': 'win',
                'network': {
                    'proxy': {
                        'type': 'HTTP',
                        'host': '127.0.0.1',
                        'port': port
                    }
                }
            }
        else:
            body = {
                'name': f'bonga_{uuid4()}',
                'browser': 'mimic',
                'os': 'win',
            }
        header = {
            'accept': 'application/json',
            'Content-Type': 'application/json'
        }
        r = requests.post(url, json.dumps(body), headers=header)
        if r.status_code == 200:
            uuid = json.loads(r.content).get('uuid')
            print(uuid)
            return uuid

    def _create_multilogin_driver(self, uuid: str) -> Remote:
        for _ in range(2):
            try:
                mla_url = f'http://127.0.0.1:{self.PORT}/api/v1/profile/start?automation=true&profileId='+uuid
                resp = requests.get(mla_url)
                r_json = resp.json()
                print(r_json)
                options = Options()
                options.add_argument('--disable-gpu')
                options.add_argument('--headless=new')
                driver = Remote(
                    command_executor=r_json['value'], options=options)
                return driver
            except KeyError:
                continue
        else:
            raise Exception('cannot create multilogin driver')

    def _create_multilogin_proxy_driver(self, idx: int) -> Remote:
        uuid = self._create_profile(idx)
        driver = self._create_multilogin_driver(uuid)
        return driver

    def _delete_profile(self, uuid: str):
        mla_url = f'http://127.0.0.1:{self.PORT}/api/v1/profile/{uuid}'
        headers = {
            'accept': 'application/json'
        }
        requests.delete(mla_url, headers=headers)

    def _stop_profile(uuid: str):
        headers = {
            'accept': 'application/json',
        }
        params = {
            'profileId': uuid,
        }
        requests.get(
            'http://localhost.multiloginapp.com:35000/api/v1/profile/stop',
            params=params,
            headers=headers
        )
