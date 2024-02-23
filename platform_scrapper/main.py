from configs.file_constantns import FAKE_CANNABIS_USED
from src.manager import Manager
from utilities.file_modifier import reporter


def main():
    manager = Manager()
    manager.manage(file=FAKE_CANNABIS_USED)


if __name__ == "__main__":
    main()
