# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-01-19 14:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('KmetApp', '0006_auto_20161208_1340'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='telefonska',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='kosarica',
            name='slika',
            field=models.FileField(default='img/Kosarica/default.jpg', upload_to='img/Kosarica/'),
        ),
    ]
