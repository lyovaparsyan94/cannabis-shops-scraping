from configs.file_constantns import FAKE_CANNABIS_USED
from src.manager import Manager

manager = Manager()

if __name__ == "__main__":
    manager.manage(file=FAKE_CANNABIS_USED)
