from django.contrib import admin

from site_scraping.models import SiteData


@admin.register(SiteData)
class SiteDataAdmin(admin.ModelAdmin):
    list_display = (
        'shop',
        "service_options",
        "phone_number",
        'ecommerce_provider',
        "type_of_delivery_offered",
        "delivery_qualifications",
        "minimum_delivery_fee",
        "zones"
    )
