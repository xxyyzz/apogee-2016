# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Event', '0009_auto_20160114_1326'),
    ]

    operations = [
        migrations.RenameField(
            model_name='events',
            old_name='tag',
            new_name='tags',
        ),
    ]
