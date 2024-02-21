from configs.file_constantns import FAKE_CANNABIS_USED
from src.manager import Manager
from platform_scrapper.configs.file_constantns import ROOT_DIR, COLLECT_DIR
manager = Manager()

if __name__ == "__main__":
    manager.manage(file=FAKE_CANNABIS_USED)