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


def write_to_xlsx(data_to_write):
    if not exists('lawyers_phone_emails_file.xlsx'):
        df = pd.DataFrame(data_to_write)
        df = df.T
        df['lawyer_name'] = df.index
        df['email'] = df['email'].apply(', '.join)
        df['phone'] = df['phone'].apply(', '.join)
        df += df[['lawyer_name', 'email', 'phone']]
    else:
        df = pd.read_excel('lawyers_phone_emails_file.xlsx')
        name = list(data_to_write.keys())[0]
        data = [
            [name, ', '.join(data_to_write[name]['phone']), ', '.join(data_to_write[name]['email'])],
        ]
        df1 = pd.DataFrame(data, columns=['lawyer_name', 'email', 'phone'])
        df = pd.concat([df, df1], ignore_index=True)
    df.to_excel('lawyers_phone_emails_file.xlsx', index=False)


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
