from django.db import models


class WeedShop(models.Model):
    municipality = models.CharField(max_length=255)
    store_name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    application_status = models.TextField()

    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    map_link = models.URLField(max_length=255, null=True, blank=True)

    store_url = models.URLField(null=True, blank=True)
    phone_number = models.CharField(max_length=255, null=True, blank=True)

    service_options = models.JSONField(default=list)  # delivery, pickup, curb-site pickup
    type_of_delivery_offered = models.JSONField(default=list)  # Instant delivery, Timeslot delivery, Same-day delivery

    contact_page = models.CharField(max_length=255, null=True, blank=True, verbose_name='contact or stores page')

    delivery_page = models.CharField(max_length=255, null=True, blank=True, verbose_name='delivery or checkout page')
    order_page = models.CharField(max_length=255, null=True, blank=True, verbose_name='order page')

    ecommerce_provider = models.TextField(null=True, blank=True)  # Dutchie, Buddi, Leafly, Weedmaps | from checkout page/shop page, can be in footer
    delivery_qualifications = models.TextField(null=True, blank=True)  # Minimum order amount, minimum order amount by zone (kilometers)
    #  it can be offered from checkout pages

    minimum_delivery_fee = models.IntegerField(null=True, blank=True)
    zones = models.TextField(null=True, blank=True)
    # idk how to get it