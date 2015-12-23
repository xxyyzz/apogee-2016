# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Event', '0002_auto_20151223_0954'),
    ]

    operations = [
        migrations.AddField(
            model_name='events',
            name='online_reg',
            field=models.NullBooleanField(),
        ),
    ]
