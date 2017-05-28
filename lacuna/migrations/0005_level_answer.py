# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lacuna', '0004_auto_20160212_1911'),
    ]

    operations = [
        migrations.AddField(
            model_name='level',
            name='answer',
            field=models.CharField(max_length=500, null=True, blank=True),
        ),
    ]
