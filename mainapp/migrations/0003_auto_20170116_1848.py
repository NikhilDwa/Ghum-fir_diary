# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-16 13:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_journal_journal_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='journal',
            name='journal_title',
            field=models.CharField(blank=True, max_length=140),
        ),
    ]