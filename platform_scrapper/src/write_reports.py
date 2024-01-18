import os
import json
import pprint


def clean_data(list_of_circle_sections, store="aaa", address='bb'):
    final_data = {}
    for item in list_of_circle_sections:
        if str(item)[0].isdigit():
            if type(list_of_circle_sections[item]) is list:
                final_data[item] = list_of_circle_sections[item]
        if type(item) is dict:
            # if type(list_of_circle_sections[item]) is dict:
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

    filename = str(store) + str(address)
    if len(res) > 0:
        with open(f"gd_{filename}.json", 'w') as file:
            json.dump(res, file, indent=2)
        print('res is: ', res)
    return res


def write_report(global_data, store, address, status, url, ecom_provider, service_options, index):
    store_l = str(store).capitalize()
    address_l = str(address).capitalize()
    filename = store_l + address_l
    liner = f"\n{60 * '-'}\n"
    with open(f"{index}glob.txt", "w") as file:
        if not global_data:
            result = f"Delivery info for {store} at address {address} NOT Found from {ecom_provider} ecommerse provider's server"
            json.dump(result, file, indent=2)
        else:
            json.dump(global_data, file, indent=2)
    with open(f"{index}{filename}.txt", "a") as f:
        report = f"Store - {store}{liner}Address - {address}{liner}{status}{liner}URL {url}{liner}Platform - {ecom_provider}{liner}Service options\n{service_options}{liner}Delivery Zones according to the price\nfirst number is the price, and in brackets are the coordinates of area according to that price \n"
        f.write(report)
        with open(f'{index}glob.txt', 'r') as glob_file:
            for line in glob_file:
                f.write(line)
    os.remove(f'{index}glob.txt')


x = ...

clean_data(x)
# clean_data(null, "null31 CELINA ST", "The Peace Pipe")

