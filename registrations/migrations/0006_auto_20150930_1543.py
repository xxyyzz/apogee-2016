# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import registrations.models


class Migration(migrations.Migration):

    dependencies = [
        ('registrations', '0005_auto_20150929_1745'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='upload',
        ),
        migrations.AddField(
            model_name='project',
            name='abstract',
            field=models.FileField(default=None, upload_to=registrations.models.upload_project),
        ),
        migrations.AlterField(
            model_name='paper',
            name='abstract',
            field=models.FileField(default=None, upload_to=registrations.models.upload_paper),
        ),
    ]
