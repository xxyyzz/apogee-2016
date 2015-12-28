# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Event', '0007_auto_20151224_1826'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='events',
            name='venue',
        ),
        migrations.AlterField(
            model_name='events',
            name='short_description',
            field=models.CharField(max_length=400),
        ),
    ]
