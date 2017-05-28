# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lacuna', '0006_auto_20160213_0942'),
    ]

    operations = [
        migrations.CreateModel(
            name='Participant',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fbid', models.BigIntegerField()),
                ('name', models.CharField(max_length=200)),
                ('score', models.IntegerField(default=0)),
                ('current_dvm_level', models.PositiveSmallIntegerField(default=1)),
                ('start_time', models.DateTimeField()),
                ('dvm_1_time', models.DurationField(null=True)),
                ('dvm_2_time', models.DurationField(null=True)),
                ('dvm_3_time', models.DurationField(null=True)),
                ('dvm_4_time', models.DurationField(null=True)),
                ('dvm_5_time', models.DurationField(null=True)),
                ('dvm_6_time', models.DurationField(null=True)),
                ('dvm_7_time', models.DurationField(null=True)),
                ('dvm_8_time', models.DurationField(null=True)),
                ('dvm_9_time', models.DurationField(null=True)),
                ('dvm_10_time', models.DurationField(null=True)),
                ('dvm_11_time', models.DurationField(null=True)),
                ('dvm_12_time', models.DurationField(null=True)),
                ('informals_stats', models.CharField(default=b'000000000000', max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='Lacuna',
        ),
    ]
