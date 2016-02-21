# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0010_auto_20160219_2240'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='team',
            name='rank',
        ),
        migrations.AddField(
            model_name='team',
            name='comments',
            field=models.CharField(default=None, max_length=200, null=True, blank=True),
        ),
    ]
