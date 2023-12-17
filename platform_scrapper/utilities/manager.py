from platform_scrapper.helpers.file_handler import load_xlsx, write_to_xlsx, save_unfilled_data, \
    remove_from_unfilled_data


class Manager:
    def __init__(self):
        ...

    def start(self):
        df = load_xlsx(file="test_cannabis.xlsx")
        # state, store, address, website, provider, service_options, phone, type_of_delivery, delivery_qualifications, min_fee, zones = df.iterrows()
        for index, row in df.iterrows():
            state = row.iloc[0]
            store = row.iloc[1]
            address = row.iloc[2]
            status = row.iloc[3]
            url = row.iloc[4]
            provider = row.iloc[5]
            haz_zone_options = row.iloc[6]
            service_options = row.iloc[7]
            phone = row.iloc[8]
            type_of_delivery_offered = row.iloc[9]
            delivery_qualifications = row.iloc[10]
            delivery_qualifications = row.iloc[10]
            min_delivery_fee = row.iloc[11]
            zones = row.iloc[12]

            # update excel values to new
            # df.at[index, 'Has Zone Options'] = '123456'
            # df.fillna('', inplace=False)
            # df.to_excel('file.xlsx', index=False)


manager = Manager()
manager.start()
