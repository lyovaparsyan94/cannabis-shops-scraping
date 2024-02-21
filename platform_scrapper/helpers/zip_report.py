import zipfile
import os


def zip_files(path_to_txt_files, path_to_result_file):
    with zipfile.ZipFile(path_to_result_file, 'w', zipfile.ZIP_DEFLATED) as zip_file:
        for root, dirs, files in os.walk(path_to_txt_files):
            for file in files:
                file_path = os.path.join(root, file)
                zip_file.write(file_path, os.path.relpath(file_path, path_to_txt_files))


path_to_files = r"../CANNABIS_RESULTS/collected_shops"
path_to_zip = r"../data/collected_shops.zip"
zip_files(path_to_files, path_to_zip)
