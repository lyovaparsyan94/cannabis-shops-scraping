import os
import json
from platform_scrapper.configs.file_constantns import COLLECT_DIR


def file_name_maker(store, address):
    filename = f"{store} {address}"
    filename = ''.join(char for char in filename if char.isalnum() or char.isspace())
    return filename


def clean_data(list_of_circle_sections, store="aaa", address='bb', reporter=None):
    final_data = {}
    for item in list_of_circle_sections:
        if str(item)[0].isdigit():
            if type(list_of_circle_sections[item]) is list:
                final_data[item] = list_of_circle_sections[item]
        if type(item) is dict:
            for key, value in item.items():
                if key:
                    for k1, v1 in value.items():
                        max_distance = max(v1.keys())
                        if key not in final_data:
                            final_data[key] = {}
                        if k1 not in final_data[key]:
                            final_data[key][k1] = {}
                        final_data[key][k1][max_distance] = v1[max_distance]
    res = {}
    for price in final_data:
        if type(final_data[price]) is list:
            res = final_data
            break
        if price not in res:
            res[price] = []
            for degree in final_data[price]:
                for km in final_data[price][degree]:
                    res[price].append(final_data[price][degree][km])

    # filename = str(store) + str(address)
    # if not reporter:
    #     with open(f"tmp__{filename}.json", 'w') as file:
    #         json.dump(res, file, indent=2)
    return res


def reporter(file_to_append=None, json_to_read=None, store=None, address=None, del_mode=False, auto=False,
             single_mode=False):
    storename = file_name_maker(store=store, address=address)
    if address and store:
        file_to_append = None
        print(f'searching {storename} ...')
        for file_name in os.listdir(COLLECT_DIR):
            if file_name.endswith(f"{storename}.txt") and not file_name.startswith('COPY'):
                print('txt found', file_name)
                file_to_append = file_name
            if file_name.endswith(f"{storename}.json"):
                print('json found', file_name)
                json_to_read = file_name
    if not file_to_append and json_to_read:
        print('not file_to_append and json_to_read')
        return None

    with open(fr"{COLLECT_DIR}\{json_to_read}", "r") as coord_file:
        coords = json.load(coord_file)
        cleaned_coords = clean_data(coords, store=address, address=address, reporter=True)
    # create with clean data temprorary file for beautiful report writer with jsonable indents
    with open(fr"{COLLECT_DIR}\{file_to_append}_G.txt", "w") as glob_file:
        json.dump(cleaned_coords, glob_file, indent=2)
    with open(fr"{COLLECT_DIR}\{file_to_append}", 'r') as f:
        lines = f.readlines()
        with open(fr'{COLLECT_DIR}\{storename}.txt', 'w') as file:  # save new file in copy
            for line in lines:
                if '{}' in line and line.strip() == '{}':
                    print("'{}' in line", line)
                    line = '\n'
                    with open(f"{COLLECT_DIR}\{file_to_append}_G.txt") as _g:
                        g_lines = _g.readlines()
                        for i in g_lines:
                            file.write(i)
                            continue
                file.write(line)
    print(f'Current file is {storename}.txt')
    os.remove(fr"{COLLECT_DIR}\{file_to_append}_G.txt")
    if del_mode:
        if not auto:
            del_mode = input(f'Confirm Delete {file_to_append} and {json_to_read}? ')
        if del_mode == 'yes' or auto:
            os.remove(file_to_append)
            os.remove(json_to_read)
            print(f'removed {file_to_append} and {json_to_read}')