# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lacuna', '0012_story'),
    ]

    operations = [
        migrations.AddField(
            model_name='participant',
            name='informals_score',
            field=models.IntegerField(default=0),
        ),
    ]
