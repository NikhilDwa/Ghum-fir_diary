# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-29 07:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0007_auto_20170129_1256'),
    ]

    operations = [
        migrations.AlterField(
            model_name='journal',
            name='date',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='journal',
            name='time',
            field=models.CharField(default='', max_length=10),
        ),
    ]
