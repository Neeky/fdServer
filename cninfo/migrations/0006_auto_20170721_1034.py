# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-07-21 10:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cninfo', '0005_auto_20170721_1013'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='companyFax',
            field=models.CharField(default='', help_text='公司传真', max_length=16),
        ),
        migrations.AddField(
            model_name='company',
            name='companyPhone',
            field=models.CharField(default='', help_text='公司电话', max_length=16),
        ),
        migrations.AddField(
            model_name='company',
            name='companyWebsite',
            field=models.CharField(default='', help_text='公司网址', max_length=32),
        ),
        migrations.AddField(
            model_name='company',
            name='ipoPERate',
            field=models.DecimalField(decimal_places=2, default=0, help_text='发行市盈率', max_digits=6),
        ),
        migrations.AddField(
            model_name='company',
            name='issueMode',
            field=models.CharField(default='', help_text='发行方式', max_length=16),
        ),
        migrations.AddField(
            model_name='company',
            name='issuePrice',
            field=models.DecimalField(decimal_places=4, default=0, help_text='发行价格', max_digits=8),
        ),
        migrations.AddField(
            model_name='company',
            name='issueRecommender',
            field=models.CharField(default='', help_text='上市推荐人', max_length=16),
        ),
        migrations.AddField(
            model_name='company',
            name='issuedQuantity',
            field=models.DecimalField(decimal_places=0, default=0, help_text='发行数量', max_digits=12),
        ),
        migrations.AddField(
            model_name='company',
            name='leadUnderwrite',
            field=models.CharField(default='', help_text='主承销商', max_length=16),
        ),
        migrations.AddField(
            model_name='company',
            name='listingTime',
            field=models.DateTimeField(default='1000-01-01 01:01:01', help_text='上市时间'),
        ),
        migrations.AddField(
            model_name='company',
            name='postalCode',
            field=models.CharField(default='', help_text='邮政编码', max_length=8),
        ),
        migrations.AddField(
            model_name='company',
            name='prospectusTime',
            field=models.DateTimeField(default='1000-01-01 01:01:01', help_text='招股时间'),
        ),
        migrations.AddField(
            model_name='company',
            name='sponsor',
            field=models.CharField(default='', help_text='保荐机构', max_length=16),
        ),
    ]
