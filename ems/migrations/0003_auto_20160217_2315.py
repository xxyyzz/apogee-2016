# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ems', '0002_auto_20160217_0112'),
    ]

    operations = [
        migrations.AddField(
            model_name='level',
            name='is_protected',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='level',
            name='judges',
            field=models.ManyToManyField(to='ems.Judge', blank=True),
        ),
        migrations.AlterField(
            model_name='level',
            name='teams',
            field=models.ManyToManyField(related_name='levels', to='backend.Team', blank=True),
        ),
    ]
