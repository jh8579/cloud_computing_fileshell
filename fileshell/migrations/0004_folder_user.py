# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-08 02:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fileshell', '0003_auto_20180607_1443'),
    ]

    operations = [
        migrations.AddField(
            model_name='folder',
            name='user',
            field=models.CharField(default='', max_length=20),
        ),
    ]