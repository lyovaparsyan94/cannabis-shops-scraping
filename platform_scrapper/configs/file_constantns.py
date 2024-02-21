import os
from os.path import abspath, dirname, join

ROOT_DIR = os.getcwd()
CONFIGS_DIR = abspath(dirname(__file__))
CONFIG_FILE_PATH = join(CONFIGS_DIR, 'config.yaml')
FAKE_CANNABIS_USED = join(ROOT_DIR, join('data', 'fake_cannabis_used_IDs.xlsx'))
CANNANBIS_USED_IDS = join(ROOT_DIR, join('data', 'cannabis_used_IDs.xlsx'))

COLLECT_DIR = join(ROOT_DIR, join('data', 'collection'))
