import csv

from django.db import migrations
from django.apps import apps


def add_table_data(apps, schema) -> None:
    WeedShop = apps.get_model('google', 'WeedShop')
    csv_file_path = 'docs/input.csv'
    with open(csv_file_path, 'r', newline='', encoding='utf-8') as csvfile:
        csv_reader = csv.reader(csvfile)
        next(csv_reader)
        for row in csv_reader:
            WeedShop.objects.create(
                municipality=row[0],
                store_name=row[1],
                address=row[2],
                application_status=row[3]
            )


class Migration(migrations.Migration):

    dependencies = [
        ('google', '0002_rename_weedshops_weedshop'),
    ]

    operations = [
        migrations.RunPython(
            code=add_table_data,
            reverse_code=migrations.RunPython.noop,
        )
    ]
