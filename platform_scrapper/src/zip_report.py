import zipfile
import os

def zip_files(path_to_files, path_to_zip):
    with zipfile.ZipFile(path_to_zip, 'w', zipfile.ZIP_DEFLATED) as zip_file:
        for root, dirs, files in os.walk(path_to_files):
            for file in files:
                file_path = os.path.join(root, file)
                zip_file.write(file_path, os.path.relpath(file_path, path_to_files))

path_to_files = r"C:\Users\1\OneDrive\Рабочий стол\DOT\cannabis-shops-scraping\platform_scrapper\CANNABIS_RESULTS\collected_data"
path_to_zip = r"C:\Users\1\OneDrive\Рабочий стол\DOT\cannabis-shops-scraping\platform_scrapper\data\collected_data.zip"
zip_files(path_to_files, path_to_zip)

