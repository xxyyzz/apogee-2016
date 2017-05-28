# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0005_auto_20160212_0807'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Update',
            new_name='Updates',
        ),
    ]
