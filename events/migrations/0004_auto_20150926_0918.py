# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_notification'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='short_description',
            field=models.CharField(max_length=140, blank=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='description',
            field=models.CharField(max_length=200, blank=True),
        ),
    ]
