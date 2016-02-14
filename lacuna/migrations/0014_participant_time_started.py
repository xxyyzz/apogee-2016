# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lacuna', '0013_participant_informals_score'),
    ]

    operations = [
        migrations.AddField(
            model_name='participant',
            name='time_started',
            field=models.DateTimeField(default=None, null=True, blank=True),
        ),
    ]
