# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2016-07-15 17:25
from __future__ import unicode_literals

import builtins
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('KmetApp', '0002_auto_20160715_1918'),
    ]

    operations = [
        migrations.CreateModel(
            name='Oglas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ime_O', models.CharField(max_length=50)),
                ('cena_O', models.IntegerField()),
                ('kolicina_O', models.IntegerField()),
                ('opis_O', models.CharField(max_length=500)),
                ('prodajalec_O', models.ForeignKey(on_delete=builtins.id, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'indexes': [],
            },
        ),
    ]
