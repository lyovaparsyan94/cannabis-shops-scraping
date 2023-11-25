from django.contrib import admin

from delivery.models import DeliveryData


@admin.register(DeliveryData)
class DeliveryDataAdmin(admin.ModelAdmin):
    list_display = (
        'shop',
        "ecommerce_provider",
        "type_of_delivery_offered",
        "delivery_qualifications",
        "minimum_delivery_fee",
        "zones"
    )
