# Generated by Django 4.2.4 on 2023-09-06 11:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shopdemo', '0005_commodity_detail_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='commodity',
            name='detail_url',
        ),
    ]