# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Event', '0005_remove_events_online_reg'),
    ]

    operations = [
        migrations.RenameField(
            model_name='events',
            old_name='content',
            new_name='short_description',
        ),
        migrations.RemoveField(
            model_name='events',
            name='contact',
        ),
        migrations.RemoveField(
            model_name='events',
            name='overview',
        ),
    ]
