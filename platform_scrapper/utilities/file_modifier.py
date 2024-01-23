import os
import json
from os.path import abspath, dirname, join

from platform_scrapper.src.write_reports import clean_data


def reporter(file_to_append=None, json_to_read=None, store=None, address=None, del_mode=False, auto=False, single_mode=False):
    src = r'C:\Users\1\OneDrive\Рабочий стол\DOT\cannabis-shops-scraping\platform_scrapper\utilities'

    if address and store:
        store1 = str(store).replace(" ", '_').replace("'", '').capitalize()
        address1 = str(address).replace(" ", '_').replace("'", '').capitalize()
        storename = store1 + address1
        file_to_append = None
        print(f'searching {storename} ...')
        for file_name in os.listdir(src):
            if file_name.endswith(f"{storename}.txt") and not file_name.startswith('COPY'):
                print('txt found', file_name)
                file_to_append = file_name
            if file_name.endswith(f"{storename}.json"):
                print('json found', file_name)
                json_to_read = file_name
    if not file_to_append and json_to_read:
        print('not file_to_append and json_to_read')
        return None

    with open(json_to_read, "r") as coord_file:
        coords = json.load(coord_file)
        cleaned_coords = clean_data(coords, store=address, address=address, reporter=True)
    # create with clean data temprorary file for beautiful report writer with jsonable indents
    with open(f"{file_to_append}_G.txt", "w") as glob_file:
        json.dump(cleaned_coords, glob_file, indent=2)
    with open(file_to_append, 'r') as f:
        lines = f.readlines()
        with open(f'{store} {address}.txt', 'w') as file:  # save new file in copy
            for line in lines:
                if '{}' in line and line.strip() == '{}':
                    print("'{}' in line", line)
                    line = '\n'
                    with open(f"{file_to_append}_G.txt") as _g:
                        g_lines = _g.readlines()
                        for i in g_lines:
                            file.write(i)
                            continue
                file.write(line)
    print(f'Current file is {store} {address}.txt')
    os.remove(f"{file_to_append}_G.txt")
    if del_mode:
        if not auto:
            del_mode = input(f'Confirm Delete {file_to_append} and {json_to_read}? ')
        if del_mode == 'yes' or auto:
            os.remove(file_to_append)
            os.remove(json_to_read)
            print(f'removed {file_to_append} and {json_to_read}')


# reporter(store="TOKE CANNABIS", address='247 CENTENNIAL PKY N UNIT 2', del_mode=False)
# reporter(file_to_append="38Spark_cannabis_24_toronto_st_n.txt", json_to_read='t_Spark_cannabis_24_toronto_st_n.json', del_mode=True)

# filename = 'TOKE CANNABIS 247 CENTENNIAL PKY N UNIT 2.txt'
# ROOT_DIR = os.getcwd()
# CONFIGS_DIR = abspath(dirname(__file__))
# FILE_DIR =join(CONFIGS_DIR, filename)
# print(ROOT_DIR)