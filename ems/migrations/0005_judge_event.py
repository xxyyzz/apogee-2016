# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Event', '0046_auto_20160218_1656'),
        ('ems', '0004_auto_20160218_0020'),
    ]

    operations = [
        migrations.AddField(
            model_name='judge',
            name='event',
            field=models.ForeignKey(default=1, to='Event.Event'),
            preserve_default=False,
        ),
    ]
