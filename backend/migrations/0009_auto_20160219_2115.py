# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0008_auto_20160218_1403'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participant',
            name='aadhaar',
            field=models.CharField(default=None, max_length=8, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='participant',
            name='address',
            field=models.TextField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='participant',
            name='bank_account_no',
            field=models.CharField(max_length=20, blank=True),
        ),
        migrations.AlterField(
            model_name='participant',
            name='bank_ifsc',
            field=models.CharField(max_length=11, blank=True),
        ),
        migrations.AlterField(
            model_name='participant',
            name='bank_name',
            field=models.CharField(max_length=200, blank=True),
        ),
        migrations.AlterField(
            model_name='participant',
            name='city',
            field=models.CharField(max_length=20, blank=True),
        ),
    ]
