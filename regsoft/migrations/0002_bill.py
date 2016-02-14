# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0007_auto_20160213_0806'),
        ('regsoft', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('amount', models.IntegerField(default=0)),
                ('given', models.IntegerField(default=0)),
                ('balance', models.IntegerField(default=0)),
                ('notes_1000', models.IntegerField(default=0, null=True, blank=True)),
                ('notes_500', models.IntegerField(default=0, null=True, blank=True)),
                ('notes_100', models.IntegerField(default=0, null=True, blank=True)),
                ('notes_50', models.IntegerField(default=0, null=True, blank=True)),
                ('notes_20', models.IntegerField(default=0, null=True, blank=True)),
                ('notes_10', models.IntegerField(default=0, null=True, blank=True)),
                ('draft_number', models.CharField(default=b'', max_length=100)),
                ('participant', models.ForeignKey(blank=True, to='backend.Participant', null=True)),
            ],
        ),
    ]
