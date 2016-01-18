# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Event', '0012_auto_20160117_2002'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='org',
            field=models.ForeignKey(default=None, blank=True, to='Event.Organization', null=True),
        ),
    ]
