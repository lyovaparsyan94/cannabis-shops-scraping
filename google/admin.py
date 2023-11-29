from django.contrib import admin

from google.models import WeedShop


@admin.register(WeedShop)
class WeedShopAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        # 'municipality',
        'store_name',
        'address',
        # 'application_status',
        'store_url'
    )
    list_display_links = ('pk',)
    search_fields = ['store_name',]
