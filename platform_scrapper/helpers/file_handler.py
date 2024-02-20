import os.path
from os.path import join, exists
import yaml
import pandas as pd
import json


def load_config(file):
    with open(file) as stream:
        config = yaml.safe_load(stream=stream)
    return config


def load_xlsx(file):
    return pd.read_excel(file)


def save_unfilled_data(person, university, filename):
    filename = filename
    info = {person: university}
    if os.path.isfile(filename):
        with open(filename, "r+") as file:
            data = json.load(file)
            if data:
                data['unfilled_data'].update(info)
            else:
                data = {"unfilled_data": info}
            print(data)
            file.seek(0)
            json.dump(data, file, indent=4)
            file.truncate()

    else:
        with open(filename, 'w') as file:
            data = {"unfilled_data": info}
            json.dump(data, file, indent=4)
            print('Data saved:', data)


def remove_from_unfilled_data(person, filename):
    with open(filename, 'r+') as file:
        all_data = json.load(file)
        if person in all_data['unfilled_data']:
            if all_data['unfilled_data'].pop(person, None):
                print(f"{person} removed from unfilled data", )
            else:
                print(f" {person} not in {all_data['unfilled_data']}")
