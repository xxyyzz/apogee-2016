# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('revengg', '0002_auto_20160214_1504'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participant',
            name='score',
            field=models.IntegerField(default=0),
        ),
    ]
