# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-27 12:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('KmetApp', '0001_initial'),
    ]

    operations = [
            migrations.AddField(
            model_name='oglas',
            name='slika',
            field=models.ImageField(default='img/Oglas/default.jpg', upload_to='img/Oglas/'),
        ),
    ]