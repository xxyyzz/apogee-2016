# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0004_auto_20160203_2202'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Updates',
            new_name='Update',
        ),
        migrations.AddField(
            model_name='participant',
            name='is_bitsian',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='team',
            name='rank',
            field=models.PositiveSmallIntegerField(default=None, null=True, blank=True),
        ),
    ]
