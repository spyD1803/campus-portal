# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-02-26 17:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administration', '0008_auto_20170226_1138'),
    ]

    operations = [
        migrations.AlterField(
            model_name='creditdetails',
            name='file',
            field=models.FileField(upload_to=''),
        ),
    ]
