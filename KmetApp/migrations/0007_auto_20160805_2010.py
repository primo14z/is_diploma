# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2016-08-05 18:10
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('KmetApp', '0006_narocilo_o'),
    ]

    operations = [
        migrations.AddField(
            model_name='narocilo_o',
            name='datum_N_O_obdelano',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='oglas',
            name='aktiven_O',
            field=models.BooleanField(default=True),
        ),
    ]
