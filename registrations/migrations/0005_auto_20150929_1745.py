# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import registrations.models


class Migration(migrations.Migration):

    dependencies = [
        ('registrations', '0004_auto_20150929_1733'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paper',
            name='abstract',
            field=models.FileField(default=None, upload_to=registrations.models.upload_dir),
        ),
    ]
