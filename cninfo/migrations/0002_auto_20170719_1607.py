# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-07-19 16:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cninfo', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='companyinfo',
            name='id',
        ),
        migrations.AlterField(
            model_name='companyinfo',
            name='stockCode',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
