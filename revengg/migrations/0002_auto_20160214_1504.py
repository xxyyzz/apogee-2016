# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('revengg', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participant',
            name='score',
            field=models.PositiveSmallIntegerField(default=0),
        ),
    ]
