# Generated by Django 2.2.5 on 2019-10-08 15:28

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0009_auto_20191004_2031'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2019, 10, 8, 15, 28, 31, 535093, tzinfo=utc)),
        ),
    ]
