# Generated by Django 3.2.23 on 2023-11-25 10:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('site_scraping', '0005_sitedata_contact_page'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sitedata',
            name='dispensary_name',
        ),
    ]
