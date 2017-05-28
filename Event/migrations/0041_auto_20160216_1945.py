# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Event', '0040_auto_20160215_1000'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='is_displayed',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='org',
            field=models.ForeignKey(default=None, blank=True, to='Event.Organization', null=True),
        ),
    ]
