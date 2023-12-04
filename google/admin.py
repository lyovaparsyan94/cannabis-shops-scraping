import csv
from django.contrib import admin

from google.models import WeedShop
from django.http import HttpResponse

from site_scraping.converter import get_row


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

    actions = ['export_csv']

    def export_csv(modeladmin, request, queryset):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=output.csv'
        csv_writer = csv.writer(response, delimiter='|')
        csv_writer.writerow([
            'Municipality or First Nation', 'Store Name', 'Address', 'Store Application Status',
            'website', 'service options', 'phone_number', 'ecommerce provider', 'type of delivery offered',
            'delivery qualifications', 'minimum delivery fee', 'zones'
        ])
        for row in queryset:
            row_rough = get_row(row)
            row = list(row_rough.values())
            csv_writer.writerow(row)
        return response
