# Generated by Django 3.2.23 on 2023-11-25 02:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WeedShops',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('municipality', models.CharField(max_length=255)),
                ('store_name', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('application_status', models.TextField()),
                ('store_url', models.URLField(blank=True, null=True)),
            ],
        ),
    ]
