# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-29 12:05
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cninfo', '0010_company_lastupdate'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='lastUPdate',
        ),
        migrations.AddField(
            model_name='company',
            name='lastUpdate',
            field=models.DateTimeField(default=datetime.datetime(2017, 7, 29, 12, 5, 37, 620342), help_text='招股时间'),
        ),
    ]
