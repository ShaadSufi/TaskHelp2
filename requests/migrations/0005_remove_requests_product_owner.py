# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2019-09-23 19:29
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('requests', '0004_auto_20190923_1740'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='requests',
            name='product_owner',
        ),
    ]
