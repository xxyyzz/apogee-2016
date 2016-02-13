# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lacuna', '0008_auto_20160213_1202'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participant',
            name='dvm_10_time',
            field=models.DurationField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='participant',
            name='dvm_11_time',
            field=models.DurationField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='participant',
            name='dvm_12_time',
            field=models.DurationField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='participant',
            name='dvm_1_time',
            field=models.DurationField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='participant',
            name='dvm_2_time',
            field=models.DurationField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='participant',
            name='dvm_3_time',
            field=models.DurationField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='participant',
            name='dvm_4_time',
            field=models.DurationField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='participant',
            name='dvm_5_time',
            field=models.DurationField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='participant',
            name='dvm_6_time',
            field=models.DurationField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='participant',
            name='dvm_7_time',
            field=models.DurationField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='participant',
            name='dvm_8_time',
            field=models.DurationField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='participant',
            name='dvm_9_time',
            field=models.DurationField(null=True, blank=True),
        ),
    ]
