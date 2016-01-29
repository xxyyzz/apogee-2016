# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import registrations.models


class Migration(migrations.Migration):

    dependencies = [
        ('registrations', '0014_auto_20160114_1326'),
    ]

    operations = [
        migrations.AddField(
            model_name='paper',
            name='paper',
            field=models.FileField(default=None, null=True, upload_to=registrations.models.upload_paper),
        ),
        migrations.AlterField(
            model_name='paper',
            name='abstract',
            field=models.FileField(default=None, upload_to=registrations.models.upload_paper_abstract),
        ),
    ]
