# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ems', '0006_score_is_frozen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='score',
            name='judge',
            field=models.ForeignKey(to='ems.Judge', on_delete=django.db.models.deletion.PROTECT),
        ),
        migrations.AlterField(
            model_name='score',
            name='level',
            field=models.ForeignKey(to='ems.Level', on_delete=django.db.models.deletion.PROTECT),
        ),
        migrations.AlterField(
            model_name='score',
            name='team',
            field=models.ForeignKey(to='backend.Team', on_delete=django.db.models.deletion.PROTECT),
        ),
    ]
