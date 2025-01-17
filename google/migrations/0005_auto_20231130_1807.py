# Generated by Django 3.2.23 on 2023-11-30 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('google', '0004_auto_20231126_1730'),
    ]

    operations = [
        migrations.AddField(
            model_name='weedshop',
            name='contact_page',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='contact or stores page'),
        ),
        migrations.AddField(
            model_name='weedshop',
            name='delivery_page',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='delivery or checkout page'),
        ),
        migrations.AddField(
            model_name='weedshop',
            name='delivery_qualifications',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='weedshop',
            name='ecommerce_provider',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='weedshop',
            name='minimum_delivery_fee',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='weedshop',
            name='order_page',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='order page'),
        ),
        migrations.AddField(
            model_name='weedshop',
            name='type_of_delivery_offered',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='weedshop',
            name='zones',
            field=models.TextField(blank=True, null=True),
        ),
    ]
