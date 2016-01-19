# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_participant_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participant',
            name='email_token',
            field=models.CharField(max_length=32, null=True, blank=True),
        ),
    ]
