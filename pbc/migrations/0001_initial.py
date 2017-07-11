# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-07-11 14:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MoneySupply',
            fields=[
                ('pushDate', models.DateTimeField(primary_key=True, serialize=False)),
                ('m0', models.DecimalField(decimal_places=6, max_digits=16)),
                ('m1', models.DecimalField(decimal_places=6, max_digits=16)),
                ('m2', models.DecimalField(decimal_places=6, max_digits=16)),
            ],
        ),
    ]