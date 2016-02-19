# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0009_auto_20160219_2115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participant',
            name='aadhaar',
            field=models.CharField(default=None, max_length=8, unique=True, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='participant',
            name='phone_one',
            field=models.BigIntegerField(null=True),
        ),
    ]
