# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-23 18:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cninfo', '0007_auto_20170721_1042'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='issueRecommender',
            field=models.CharField(default='', help_text='上市推荐人', max_length=32),
        ),
    ]