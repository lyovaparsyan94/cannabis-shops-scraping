import csv
from google.models import WeedShop
from site_scraping.models import SiteData


def convert_to_csv(file_name: str = 'output.csv'):
    headers = ['Municipality or First Nation', 'Store Name', 'Address', 'Store Application Status',
               'website', 'service options', 'phone_number', 'ecommerce provider', 'type of delivery offered',
               'delivery qualifications', 'minimum delivery fee', 'zones'
               ]
    with open(file_name, 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter='|')
        csv_writer.writerow(headers)
        shops = WeedShop.objects.all()
        for shop in shops:
            row_rough = get_row(shop)
            row = list(row_rough.values())
            csv_writer.writerow(row)


def get_row(shop: WeedShop) -> dict:
    row = {}
    row['Municipality or First Nation'] = ''
    row['Store Name'] = ''
    row['Address'] = ''
    row['Store Application Status'] = ''
    row['website'] = ''
    row['service options'] = ''
    row['phone_number'] = ''

    row['ecommerce provider'] = ''
    row['type of delivery offered'] = ''
    row['delivery qualifications'] = ''
    row['minimum delivery fee'] = ''
    row['zones'] = ''

    row['Municipality or First Nation'] = shop.municipality
    row['Store Name'] = shop.store_name
    row['Address'] = shop.address
    row['Store Application Status'] = shop.application_status
    if shop.store_url:
        row['website'] = shop.store_url
    if shop.service_options:
        row['service options'] = shop.service_options
    if shop.phone_number:
        row['phone_number'] = shop.phone_number
    site_datas = SiteData.objects.filter(shop=shop)
    if len(site_datas) > 0:
        site_data = site_datas[0]
        if site_data.ecommerce_provider:
            row['ecommerce provider'] = site_data.ecommerce_provider
        if site_data.type_of_delivery_offered:
            row['type of delivery offered'] = ''
        if site_data.delivery_qualifications:
            row['delivery qualifications'] = ''
        if site_data.minimum_delivery_fee:
            row['minimum delivery fee'] = ''
        if site_data.zones:
            row['zones'] = ''
    return row
