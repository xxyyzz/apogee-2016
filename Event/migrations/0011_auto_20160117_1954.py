# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Event', '0010_auto_20160117_1612'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='events',
            new_name='Event',
        ),
        migrations.RenameModel(
            old_name='Tabs',
            new_name='Tab',
        ),
    ]
