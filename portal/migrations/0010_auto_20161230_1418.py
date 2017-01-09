# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-30 08:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0009_mod'),
    ]

    operations = [
        migrations.CreateModel(
            name='Forum',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('thread_title', models.CharField(max_length=50)),
                ('thread_description', models.TextField()),
                ('thread_tag', models.CharField(max_length=15)),
                ('thread_user', models.CharField(max_length=20)),
            ],
        ),
        migrations.DeleteModel(
            name='mod',
        ),
    ]
