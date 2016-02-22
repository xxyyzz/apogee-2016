# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Event', '0050_auto_20160219_2240'),
    ]

    operations = [
        migrations.AddField(
            model_name='schedule',
            name='end_date',
            field=models.CharField(max_length=100, blank=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='org',
            field=models.ForeignKey(default=None, blank=True, to='Event.Organization', null=True),
        ),
    ]
