from django.db import models

from google.models import WeedShop


class DeliveryData(models.Model):
    shop = models.ForeignKey(WeedShop, on_delete=models.CASCADE)
    ecommerce_provider = models.TextField()  # Dutchie, Buddi, Leafly, Weedmaps
    type_of_delivery_offered = models.TextField()  # Instant delivery, Timeslot delivery, Same-day delivery
    delivery_qualifications = models.TextField()  # Minimum order amount, minimum order amount by zone (kilometers)
    minimum_delivery_fee = models.IntegerField()
    zones = models.TextField()
