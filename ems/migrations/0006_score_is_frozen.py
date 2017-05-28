# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ems', '0005_judge_event'),
    ]

    operations = [
        migrations.AddField(
            model_name='score',
            name='is_frozen',
            field=models.BooleanField(default=False),
        ),
    ]
