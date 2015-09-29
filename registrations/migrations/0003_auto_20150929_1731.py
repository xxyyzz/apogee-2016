# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registrations', '0002_auto_20150922_1757'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='paper',
            name='college',
        ),
        migrations.RemoveField(
            model_name='project',
            name='college',
        ),
        migrations.AddField(
            model_name='paper',
            name='abstract',
            field=models.FileField(default=None, upload_to=b'papers'),
        ),
        migrations.AlterField(
            model_name='paper',
            name='stub',
            field=models.CharField(unique=True, max_length=8),
        ),
        migrations.AlterField(
            model_name='project',
            name='stub',
            field=models.CharField(unique=True, max_length=8),
        ),
    ]
