# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-17 02:19
from __future__ import unicode_literals

import cars.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0004_auto_20170217_0132'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='user',
            field=models.ForeignKey(default=1, on_delete=models.SET(cars.models.set_delete_user), to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
