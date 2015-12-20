# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registrations', '0012_auto_20151128_0824'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='assoc',
            field=models.ForeignKey(to='registrations.Association', null=True),
        ),
    ]
