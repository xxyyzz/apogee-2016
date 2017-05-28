# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lacuna',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fbid', models.BigIntegerField()),
                ('name', models.CharField(max_length=200)),
                ('score', models.IntegerField(default=0)),
                ('current_dvm_level', models.PositiveSmallIntegerField(default=1)),
                ('current_informals_level', models.PositiveSmallIntegerField(default=1)),
                ('start_time', models.DateTimeField()),
                ('dvm_1_time', models.IntegerField()),
                ('dvm_2_time', models.IntegerField()),
                ('dvm_3_time', models.IntegerField()),
                ('dvm_4_time', models.IntegerField()),
                ('dvm_5_time', models.IntegerField()),
                ('dvm_6_time', models.IntegerField()),
                ('dvm_7_time', models.IntegerField()),
                ('dvm_8_time', models.IntegerField()),
                ('dvm_9_time', models.IntegerField()),
                ('dvm_10_time', models.IntegerField()),
                ('dvm_11_time', models.IntegerField()),
                ('dvm_12_time', models.IntegerField()),
            ],
        ),
    ]
