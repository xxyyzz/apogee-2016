# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registrations', '0013_auto_20151217_1104'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paper',
            name='status',
            field=models.CharField(max_length=2, choices=[('1', 'Round 1'), ('2', 'Round 2'), ('3', 'Round 3')], default='1'),
        ),
        migrations.AlterField(
            model_name='project',
            name='status',
            field=models.CharField(max_length=2, choices=[('1', 'Round 1'), ('2', 'Round 2'), ('3', 'Round 3')], default='1'),
        ),
    ]
