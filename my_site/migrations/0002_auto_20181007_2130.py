# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-10-07 13:30
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_site', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UesrInfo',
            new_name='UserInfo',
        ),
    ]
