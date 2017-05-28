# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0010_auto_20160219_2240'),
    ]

    operations = [
        migrations.AddField(
            model_name='participant',
            name='barcode',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
    ]
