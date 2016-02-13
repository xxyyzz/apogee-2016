# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lacuna', '0005_level_answer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lacuna',
            name='current_informals_level',
        ),
        migrations.RemoveField(
            model_name='lacuna',
            name='informals_1',
        ),
        migrations.RemoveField(
            model_name='lacuna',
            name='informals_10',
        ),
        migrations.RemoveField(
            model_name='lacuna',
            name='informals_11',
        ),
        migrations.RemoveField(
            model_name='lacuna',
            name='informals_12',
        ),
        migrations.RemoveField(
            model_name='lacuna',
            name='informals_2',
        ),
        migrations.RemoveField(
            model_name='lacuna',
            name='informals_3',
        ),
        migrations.RemoveField(
            model_name='lacuna',
            name='informals_4',
        ),
        migrations.RemoveField(
            model_name='lacuna',
            name='informals_5',
        ),
        migrations.RemoveField(
            model_name='lacuna',
            name='informals_6',
        ),
        migrations.RemoveField(
            model_name='lacuna',
            name='informals_7',
        ),
        migrations.RemoveField(
            model_name='lacuna',
            name='informals_8',
        ),
        migrations.RemoveField(
            model_name='lacuna',
            name='informals_9',
        ),
        migrations.AddField(
            model_name='lacuna',
            name='informals_stats',
            field=models.CharField(default=b'[0,0,0,0,0,0,0,0,0,0,0,0]', max_length=100),
        ),
    ]
