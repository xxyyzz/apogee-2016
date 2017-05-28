# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Event', '0003_events_online_reg'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='events',
            name='date',
        ),
        migrations.RemoveField(
            model_name='events',
            name='endingtime',
        ),
        migrations.RemoveField(
            model_name='events',
            name='startingtime',
        ),
    ]
