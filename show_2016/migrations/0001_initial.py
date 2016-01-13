# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Entries',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('zip', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
                ('pic1_title', models.CharField(max_length=100)),
                ('pic2_title', models.CharField(max_length=100)),
                ('pic3_title', models.CharField(max_length=100)),
                ('pic4_title', models.CharField(max_length=100)),
                ('pic5_title', models.CharField(max_length=100)),
                ('pic6_title', models.CharField(max_length=100)),
                ('pic7_title', models.CharField(max_length=100)),
                ('pic8_title', models.CharField(max_length=100)),
                ('pic1_category', models.CharField(max_length=100)),
                ('pic2_category', models.CharField(max_length=100)),
                ('pic3_category', models.CharField(max_length=100)),
                ('pic4_category', models.CharField(max_length=100)),
                ('pic5_category', models.CharField(max_length=100)),
                ('pic6_category', models.CharField(max_length=100)),
                ('pic7_category', models.CharField(max_length=100)),
                ('pic8_category', models.CharField(max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
