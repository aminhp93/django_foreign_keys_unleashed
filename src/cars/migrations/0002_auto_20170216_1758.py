# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-16 17:58
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cars', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car',
            name='user',
        ),
        migrations.AddField(
            model_name='car',
            name='driver',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
