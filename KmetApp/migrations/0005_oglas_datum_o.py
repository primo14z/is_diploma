# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2016-07-15 23:37
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('KmetApp', '0004_auto_20160715_1931'),
    ]

    operations = [
        migrations.AddField(
            model_name='oglas',
            name='datum_O',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
    ]
