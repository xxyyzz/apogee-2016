# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Event', '0039_auto_20160214_1838'),
    ]

    operations = [
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.CharField(max_length=100, blank=True)),
                ('startingtime', models.CharField(max_length=100, blank=True)),
                ('endingtime', models.CharField(max_length=100, blank=True)),
                ('venue', models.CharField(max_length=100, blank=True)),
                ('round_no', models.CharField(max_length=100, blank=True)),
            ],
        ),
        migrations.AlterField(
            model_name='event',
            name='org',
            field=models.ForeignKey(default=None, blank=True, to='Event.Organization', null=True),
        ),
        migrations.AddField(
            model_name='schedule',
            name='event',
            field=models.ForeignKey(to='Event.Event'),
        ),
    ]
