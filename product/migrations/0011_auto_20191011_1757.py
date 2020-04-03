# Generated by Django 2.2.5 on 2019-10-11 15:57

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0010_auto_20191008_1728'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(default=1, upload_to='product/maineImg'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2019, 10, 11, 15, 57, 33, 649495, tzinfo=utc)),
        ),
    ]
