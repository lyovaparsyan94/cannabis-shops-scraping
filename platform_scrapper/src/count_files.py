import os

path = r"C:\Users\1\OneDrive\Рабочий стол\DOT\cannabis-shops-scraping\platform_scrapper\utilities"
txt_files = [f for f in os.listdir(path) if f.endswith('.txt')]
json_files = [f for f in os.listdir(path) if f.endswith('.json')]
num_txt_files = len(txt_files)
json_files = len(json_files)

print(f"There are {num_txt_files} .json files in {path}")
print(f"There are {json_files} .json files in {path}")
