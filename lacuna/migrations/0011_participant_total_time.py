# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lacuna', '0010_auto_20160213_1412'),
    ]

    operations = [
        migrations.AddField(
            model_name='participant',
            name='total_time',
            field=models.DurationField(null=True, blank=True),
        ),
    ]
