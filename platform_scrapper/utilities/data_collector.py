import os
import json
from operator import index
from configs.file_constantns import COLLECT_DIR
from utilities.file_handler import file_name_maker


def write_report(global_data, store, address, status, url, ecom_provider, service_options, phone, index,
                 special_hours, min_delivery_fee=''):
    filename = file_name_maker(store, address)
    liner = f"\n{70 * '-'}\n"
    days = {}
    if special_hours:
        for i in special_hours:
            if i['name'] not in days:
                if i['hoursPerDay']:
                    house_perday = i['hoursPerDay'][0]
                    dayli_info = f"active - {house_perday['deliveryHours']['active']}, hours per day: from - {i['hoursPerDay'][0]['deliveryHours']['start']}, to - {i['hoursPerDay'][0]['deliveryHours']['end']}"
                else:
                    dayli_info = f"hours per day - {i['hoursPerDay']}"
                day = {f"{i['name']} at {i['startDate'][5:10]}": [dayli_info]}
                days.update(day)
    with open(rf"{COLLECT_DIR}\{index}glob.txt", "w") as file:
        if not all(global_data):
            result = f"Delivery info for {store} at address {address} NOT Found from {ecom_provider} ecommerse provider's server"
            json.dump(result, file, indent=2)
        else:
            json.dump(global_data, file, indent=2)
    with open(fr"{COLLECT_DIR}\{index}{filename}.txt", "a") as f:
        report = f"Store - {store}{liner}Address - {address}{liner}Store Application Status - {status}{liner}URL {url}{liner}Platform - {ecom_provider}{liner}Service options\n{service_options}{liner}Phone\n{phone}{liner}Delivery Zones according to the price:\nfirst number is the price, and in brackets are the coordinates of area according to that price\n{min_delivery_fee}\n"
        f.write(report)
        with open(fr"{COLLECT_DIR}\{index}glob.txt", 'r') as glob_file:
            for line in glob_file:
                f.write(line)
            f.write(f"{liner}Special days or hours:\n")
            if days:
                for i, j in days.items():
                    f.write(f"\n{i} - {j[0]}")
            else:
                f.write("- not received information about special days or hours")
            f.write(f"{liner}")
    os.remove(fr'{COLLECT_DIR}\{index}glob.txt')
    print(
        f"Wrote global_data \nto {index}{filename}.txt,\n removed json with same name and marked status to True, at index: {index}")