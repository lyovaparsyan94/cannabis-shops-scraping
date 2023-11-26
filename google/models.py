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
