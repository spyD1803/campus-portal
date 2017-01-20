# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-17 16:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='courses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_title', models.CharField(max_length=50)),
                ('course_faculty', models.CharField(max_length=50)),
                ('coursefor_ug1', models.BooleanField(default=False)),
                ('coursefor_ug2', models.BooleanField(default=False)),
                ('coursefor_ug3', models.BooleanField(default=False)),
                ('coursefor_ug4', models.BooleanField(default=False)),
                ('course_cse', models.CharField(max_length=50)),
                ('course_ece', models.CharField(max_length=50)),
            ],
        ),
    ]