# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-26 06:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0019_auto_20170226_1138'),
    ]

    operations = [
        migrations.AddField(
            model_name='credits',
            name='total_credits',
            field=models.IntegerField(default=0),
        ),
    ]
