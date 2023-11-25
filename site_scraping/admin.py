from django.contrib import admin

from site_scraping.models import SiteData


@admin.register(SiteData)
class SiteDataAdmin(admin.ModelAdmin):
    list_display = (
        'shop',
        "dispensary_name",
        "service_options",
        "phone_number"
    )
