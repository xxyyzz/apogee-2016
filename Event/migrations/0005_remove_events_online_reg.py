# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Event', '0004_auto_20151223_1945'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='events',
            name='online_reg',
        ),
    ]
