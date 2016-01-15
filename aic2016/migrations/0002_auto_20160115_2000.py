# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aic2016', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aicsubmission',
            name='problem_statement',
            field=models.CharField(max_length=500, choices=[('1', 'Schneider Electric'), ('2', 'Luminous'), ('3', 'Sterling Engineering'), ('4', 'Wooplr'), ('5', 'HarVa'), ('6', 'NextGen'), ('7', 'Bentley'), ('8', 'Techture')]),
        ),
    ]
