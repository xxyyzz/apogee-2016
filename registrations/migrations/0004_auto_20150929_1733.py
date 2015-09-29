# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registrations', '0003_auto_20150929_1731'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paper',
            name='co_author',
            field=models.ForeignKey(related_name='co_authors', blank=True, to='registrations.Participant', null=True),
        ),
    ]
