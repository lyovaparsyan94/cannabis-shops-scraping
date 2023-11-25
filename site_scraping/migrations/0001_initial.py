# Generated by Django 3.2.23 on 2023-11-25 09:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('google', '0003_move_table_to_model'),
    ]

    operations = [
        migrations.CreateModel(
            name='SiteData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dispensary_name', models.TextField()),
                ('service_options', models.TextField()),
                ('phone_number', models.CharField(max_length=255)),
                ('shop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='google.weedshop')),
            ],
        ),
    ]