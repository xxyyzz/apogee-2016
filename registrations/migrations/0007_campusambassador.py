# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registrations', '0006_auto_20150930_1543'),
    ]

    operations = [
        migrations.CreateModel(
            name='CampusAmbassador',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=400)),
                ('year', models.CharField(max_length=20)),
                ('degree', models.CharField(max_length=200)),
                ('email', models.EmailField(unique=True, max_length=254)),
                ('phone', models.BigIntegerField()),
                ('ambassador_quality', models.TextField()),
                ('root_mail', models.BooleanField(default=False)),
                ('college', models.ForeignKey(to='registrations.College')),
            ],
            options={
                'verbose_name_plural': 'Campus Ambassadors',
            },
        ),
    ]
