# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('regsoft', '0003_auto_20160220_1545'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='a',
            field=models.IntegerField(null=True, default=0),
        ),
        migrations.AddField(
            model_name='room',
            name='b',
            field=models.IntegerField(null=True, default=0),
        ),
        migrations.AddField(
            model_name='room',
            name='c',
            field=models.IntegerField(null=True, default=0),
        ),
        migrations.AddField(
            model_name='room',
            name='d',
            field=models.IntegerField(null=True, default=0),
        ),
        migrations.AddField(
            model_name='room',
            name='e',
            field=models.IntegerField(null=True, default=0),
        ),
        migrations.AddField(
            model_name='room',
            name='f',
            field=models.IntegerField(null=True, default=0),
        ),
        migrations.AlterField(
            model_name='bill',
            name='draft_number',
            field=models.CharField(default='', max_length=100),
        ),
    ]
