# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-30 14:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mentee', '0004_auto_20170430_1408'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_mentee',
            name='mentor',
            field=models.CharField(default=0, max_length=200),
        ),
    ]
