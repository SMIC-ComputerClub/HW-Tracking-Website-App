# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-03 03:22
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('log', '0004_auto_20170802_2117'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Profile',
            new_name='Setting',
        ),
    ]
