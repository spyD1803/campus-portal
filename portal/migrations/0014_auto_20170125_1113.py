# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-25 05:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0013_students'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formrequest',
            name='form_reason',
            field=models.CharField(max_length=100),
        ),
    ]
