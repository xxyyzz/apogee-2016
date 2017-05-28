# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lacuna', '0009_auto_20160213_1329'),
    ]

    operations = [
        migrations.RenameField(
            model_name='participant',
            old_name='score',
            new_name='progress',
        ),
    ]
