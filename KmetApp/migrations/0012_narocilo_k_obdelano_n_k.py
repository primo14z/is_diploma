# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2016-08-07 20:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('KmetApp', '0011_auto_20160807_2217'),
    ]

    operations = [
        migrations.AddField(
            model_name='narocilo_k',
            name='obdelano_N_K',
            field=models.BooleanField(default=False),
        ),
    ]
