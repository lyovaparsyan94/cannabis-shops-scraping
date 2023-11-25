from django.db import models
from google.models import WeedShop


class SiteData(models.Model):
    shop = models.ForeignKey(WeedShop, on_delete=models.CASCADE)

    contact_page = models.CharField(max_length=255, null=True, blank=True, verbose_name='contact or stores page')
    phone_number = models.CharField(max_length=255, null=True, blank=True)  # can get from stores page / contact page

    delivery_page = models.CharField(max_length=255, null=True, blank=True, verbose_name='delivery or checkout page')
    order_page = models.CharField(max_length=255, null=True, blank=True, verbose_name='order page')

    ecommerce_provider = models.TextField(null=True, blank=True)  # Dutchie, Buddi, Leafly, Weedmaps | from checkout page/shop page, can be in footer
    service_options = models.TextField(null=True, blank=True)  # delivery, pickup, curb-site pickup
    type_of_delivery_offered = models.TextField(null=True, blank=True)  # Instant delivery, Timeslot delivery, Same-day delivery
    delivery_qualifications = models.TextField(null=True, blank=True)  # Minimum order amount, minimum order amount by zone (kilometers)
    #  it can be offered from checkout pages

    minimum_delivery_fee = models.IntegerField(null=True, blank=True)
    zones = models.TextField(null=True, blank=True)
    # idk how to get it
