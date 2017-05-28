# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registrations', '0007_campusambassador'),
    ]

    operations = [
        migrations.AddField(
            model_name='campusambassador',
            name='pcr_approved',
            field=models.NullBooleanField(default=False),
        ),
    ]
