# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('show_2016', '0002_auto_20160110_1803'),
    ]

    operations = [
        migrations.AddField(
            model_name='entries',
            name='pic2_category',
            field=models.CharField(max_length=50, default=''),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='entries',
            name='pic3_category',
            field=models.CharField(max_length=50, default=''),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='entries',
            name='pic4_category',
            field=models.CharField(max_length=50, default=''),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='entries',
            name='pic5_category',
            field=models.CharField(max_length=50, default=''),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='entries',
            name='pic6_category',
            field=models.CharField(max_length=50, default=''),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='entries',
            name='pic7_category',
            field=models.CharField(max_length=50, default=''),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='entries',
            name='pic8_category',
            field=models.CharField(max_length=50, default=''),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='entries',
            name='pic1_category',
            field=models.CharField(max_length=50, default=''),
            preserve_default=True,
        ),
    ]
