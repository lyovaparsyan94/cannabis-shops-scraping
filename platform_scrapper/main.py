from configs.file_constantns import FAKE_CANNABIS_USED
from src.manager import Manager


def main():
    manager = Manager()
    manager.manage(file=FAKE_CANNABIS_USED)


if __name__ == "__main__":
    main()
