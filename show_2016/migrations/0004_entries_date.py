# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('show_2016', '0003_auto_20160110_2206'),
    ]

    operations = [
        migrations.AddField(
            model_name='entries',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2016, 1, 11, 22, 40, 26, 953598, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
