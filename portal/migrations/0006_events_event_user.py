# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-22 07:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0005_auto_20161222_1235'),
    ]

    operations = [
        migrations.AddField(
            model_name='events',
            name='event_user',
            field=models.CharField(default='admin', max_length=50),
            preserve_default=False,
        ),
    ]
