# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registrations', '0008_campusambassador_pcr_approved'),
    ]

    operations = [
        migrations.AddField(
            model_name='paper',
            name='status',
            field=models.CharField(default=b'0', max_length=2, choices=[(b'0', b'Submitted'), (b'1', b'Passed Round 1'), (b'2', b'Passed Round 2')]),
        ),
        migrations.AddField(
            model_name='project',
            name='status',
            field=models.CharField(default=b'0', max_length=2, choices=[(b'0', b'Submitted'), (b'1', b'Passed Round 1'), (b'2', b'Passed Round 2')]),
        ),
    ]
