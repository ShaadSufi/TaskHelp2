# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2019-09-23 14:40
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('requests', '0003_auto_20190921_0252'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='requests',
            name='from_date',
        ),
        migrations.RemoveField(
            model_name='requests',
            name='till_date',
        ),
    ]
