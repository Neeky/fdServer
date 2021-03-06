# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-09-08 16:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShiborRate',
            fields=[
                ('push_date', models.DateField(help_text='发布时间', primary_key=True, serialize=False)),
                ('one_night', models.DecimalField(decimal_places=4, help_text='隔夜利率', max_digits=16)),
                ('one_week', models.DecimalField(decimal_places=4, help_text='一周利率', max_digits=16)),
                ('two_week', models.DecimalField(decimal_places=4, help_text='两周利率', max_digits=16)),
                ('one_month', models.DecimalField(decimal_places=4, help_text='一月利率', max_digits=16)),
                ('three_month', models.DecimalField(decimal_places=4, help_text='三月利率', max_digits=16)),
                ('six_month', models.DecimalField(decimal_places=4, help_text='六月利率', max_digits=16)),
                ('nine_month', models.DecimalField(decimal_places=4, help_text='九月利率', max_digits=16)),
                ('one_year', models.DecimalField(decimal_places=4, help_text='一年利率', max_digits=16)),
            ],
        ),
    ]
