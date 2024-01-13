import os
from pprint import pprint
path = r"C:\Users\1\OneDrive\Рабочий стол\DOT\cannabis-shops-scraping\platform_scrapper\utilities"
txt_files = [f for f in os.listdir(path) if f.endswith('.txt')]
num_txt_files = len(txt_files)

print(f"There are {num_txt_files} .txt files in {path}")
pprint(os.listdir(path))