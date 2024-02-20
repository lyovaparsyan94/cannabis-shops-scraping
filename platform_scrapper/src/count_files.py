import os

path = r"C:\Users\parsy\OneDrive\Desktop\DOT\cannabis-shops-scraping\platform_scrapper\CANNABIS_RESULTS\collected_shops"
txt_files = [f for f in os.listdir(path) if f.endswith('.txt')]
json_files = [j for j in os.listdir(path) if j.endswith('.json')]
xlsx_files = [x for x in os.listdir(path) if x.endswith('.xlsx')]
num_txt_files = len(txt_files)
json_files = len(json_files)

print(f"There are {num_txt_files} .txt files in {path}")
print(f"There are {json_files} .json files in {path}")
print(f"There are {xlsx_files} .json files in {path}")
