from django.db import models
from google.models import WeedShop


class SiteData(models.Model):
    shop = models.ForeignKey(WeedShop, on_delete=models.CASCADE)
    dispensary_name = models.TextField()
    service_options = models.TextField()  # delivery, pickup, curb-site pickup
    phone_number = models.CharField(max_length=255)
