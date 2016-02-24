# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lacuna', '0014_participant_time_started'),
    ]

    operations = [
        migrations.AlterField(
            model_name='level',
            name='css_file',
            field=models.TextField(default='NA'),
        ),
        migrations.AlterField(
            model_name='level',
            name='dept',
            field=models.CharField(choices=[('DVM', 'DVM'), ('INFORMALS', 'INFORMALS')], max_length=10),
        ),
        migrations.AlterField(
            model_name='level',
            name='html_file',
            field=models.TextField(default='NA'),
        ),
        migrations.AlterField(
            model_name='level',
            name='js_file',
            field=models.TextField(default='NA'),
        ),
        migrations.AlterField(
            model_name='participant',
            name='informals_stats',
            field=models.CharField(default='000000000000', max_length=100),
        ),
        migrations.AlterField(
            model_name='story',
            name='content',
            field=models.TextField(default='NA'),
        ),
    ]
