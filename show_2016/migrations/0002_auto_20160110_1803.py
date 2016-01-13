# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('show_2016', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entries',
            name='pic2_category',
        ),
        migrations.RemoveField(
            model_name='entries',
            name='pic3_category',
        ),
        migrations.RemoveField(
            model_name='entries',
            name='pic4_category',
        ),
        migrations.RemoveField(
            model_name='entries',
            name='pic5_category',
        ),
        migrations.RemoveField(
            model_name='entries',
            name='pic6_category',
        ),
        migrations.RemoveField(
            model_name='entries',
            name='pic7_category',
        ),
        migrations.RemoveField(
            model_name='entries',
            name='pic8_category',
        ),
        migrations.AlterField(
            model_name='entries',
            name='pic1_category',
            field=models.ForeignKey(to='show_2016.Categories'),
            preserve_default=True,
        ),
    ]
