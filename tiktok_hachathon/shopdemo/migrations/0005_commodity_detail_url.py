# Generated by Django 4.2.4 on 2023-09-06 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopdemo', '0004_commodity_rec_from_friend'),
    ]

    operations = [
        migrations.AddField(
            model_name='commodity',
            name='detail_url',
            field=models.CharField(default=0, max_length=3000),
            preserve_default=False,
        ),
    ]
