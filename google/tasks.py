from django.db.models import Count


from google.models import WeedShop
from google.serp_scraper import find_all_shop_urls


def find_shop_url():
    find_all_shop_urls()


def test():
    # most_common_address = WeedShop.objects.values('address').annotate(address_count=Count('address')).order_by('-address_count').first()
    # print(most_common_address)
    shops = WeedShop.objects.filter(address='955 WESTNEY RD S, UNIT 4-II')
    for shop in shops:
        print(f'{shop.pk=}; {shop.address}; {shop.store_name=}; {shop.municipality}')
