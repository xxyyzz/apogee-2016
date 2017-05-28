# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registrations', '0011_auto_20151126_1001'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paper',
            name='status',
            field=models.CharField(default=b'1', max_length=2, choices=[(b'1', b'Round 1'), (b'2', b'Round 2'), (b'3', b'Round 3')]),
        ),
    ]
