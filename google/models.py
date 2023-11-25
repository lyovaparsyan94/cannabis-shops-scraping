from django.db import models


class WeedShop(models.Model):
    municipality = models.CharField(max_length=255)
    store_name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    application_status = models.TextField()
    store_url = models.URLField(null=True, blank=True)
