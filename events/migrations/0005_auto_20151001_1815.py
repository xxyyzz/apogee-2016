# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0004_auto_20150926_0918'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='max_team_size',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='event',
            name='max_teams',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='event',
            name='min_team_size',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='event',
            name='min_teams',
            field=models.IntegerField(default=0),
        ),
    ]
