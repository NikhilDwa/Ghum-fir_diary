# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-16 09:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='journal',
            name='journal_image',
            field=models.FileField(blank=True, upload_to=''),
        ),
    ]