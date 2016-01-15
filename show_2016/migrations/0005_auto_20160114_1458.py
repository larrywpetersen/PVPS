# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('show_2016', '0004_entries_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='entries',
            name='pic1_price',
            field=models.CharField(max_length=30, default=''),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='entries',
            name='pic2_price',
            field=models.CharField(max_length=30, default=''),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='entries',
            name='pic3_price',
            field=models.CharField(max_length=30, default=''),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='entries',
            name='pic4_price',
            field=models.CharField(max_length=30, default=''),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='entries',
            name='pic5_price',
            field=models.CharField(max_length=30, default=''),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='entries',
            name='pic6_price',
            field=models.CharField(max_length=30, default=''),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='entries',
            name='pic7_price',
            field=models.CharField(max_length=30, default=''),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='entries',
            name='pic8_price',
            field=models.CharField(max_length=30, default=''),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='entries',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2016, 1, 14, 21, 58, 49, 395872, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
