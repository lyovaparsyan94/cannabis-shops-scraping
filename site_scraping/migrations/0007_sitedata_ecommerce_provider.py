# Generated by Django 3.2.23 on 2023-11-25 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_scraping', '0006_remove_sitedata_dispensary_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='sitedata',
            name='ecommerce_provider',
            field=models.TextField(blank=True, null=True),
        ),
    ]
