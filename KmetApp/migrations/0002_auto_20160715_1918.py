# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2016-07-15 17:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('KmetApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
