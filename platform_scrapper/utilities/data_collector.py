import os
import json
import pprint


def clean_data(list_of_circle_sections, store="Nodata", address='Noaddress'):
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

    filename = str(store) + str(address)
    with open(f"gd_{filename}.json", 'w') as file:
        json.dump(res, file)
    pprint.pprint(res)
    return res


def write_report(global_data, store, address, status, url, ecom_provider, service_options, phone, index,
                 special_hours=''):
    store1 = str(store).replace(" ", '_').replace("'", '').capitalize()
    address1 = str(address).replace(" ", '_').replace("'", '').capitalize()
    filename = store1 + address1
    liner = f"\n{60 * '-'}\n"
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
    with open(f"{index}glob.txt", "w") as file:
        if not all(global_data):
            result = f"Delivery info for {store} at address {address} NOT Found from {ecom_provider} ecommerse provider's server"
            json.dump(result, file, indent=2)
        else:
            json.dump(global_data, file, indent=2)
    with open(f"{index}{filename}.txt", "a") as f:
        report = f"Store - {store}{liner}Address - {address}{liner}Store Application Status - {status}{liner}URL {url}{liner}Platform - {ecom_provider}{liner}Service options\n{service_options}{liner}Phone\n{phone}{liner}Delivery Zones according to the price:\nfirst number is the price, and in brackets are the coordinates of area according to that price\n"
        f.write(report)
        with open(f'{index}glob.txt', 'r') as glob_file:
            for line in glob_file:
                f.write(line)
            f.write(f"{liner}Special days or hours:\n")
            if days:
                for i, j in days.items():
                    f.write(f"\n{i} - {j[0]}")
            else:
                f.write("- not received information about special days or hours")
            f.write(f"{liner}")
    os.remove(f'{index}glob.txt')
    print(
        f"Wrote {global_data} to {index}{filename}.txt,\n removed json with same name and marked status to True, at index {index}")

# clean_data(x)
# clean_data(null, "null31 CELINA ST", "The Peace Pipe")
# write_report({}, 'ispace', 'erevan 13', 'open', 'blabla.com', 'Dutchie', 'custom service options', 13)
