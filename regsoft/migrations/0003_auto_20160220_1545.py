# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('regsoft', '0002_bill'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bill',
            name='participant',
        ),
        migrations.AddField(
            model_name='bill',
            name='gleader',
            field=models.CharField(max_length=10, null=True, blank=True),
        ),
    ]
