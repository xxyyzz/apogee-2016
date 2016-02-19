# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0007_auto_20160213_0806'),
    ]

    operations = [
        migrations.CreateModel(
            name='gleader',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('groupcode', models.CharField(max_length=100, null=True, blank=True)),
                ('amount_deducted', models.IntegerField(default=0, null=True)),
                ('amount_taken', models.IntegerField(default=0, null=True)),
            ],
            options={
                'verbose_name': 'Group Leader',
            },
        ),
        migrations.AddField(
            model_name='participant',
            name='bill_id',
            field=models.CharField(default=b'', max_length=10, blank=True),
        ),
        migrations.AddField(
            model_name='gleader',
            name='details',
            field=models.ForeignKey(default=None, blank=True, to='backend.Participant', null=True),
        ),
        migrations.AddField(
            model_name='participant',
            name='grpleader',
            field=models.ForeignKey(default=None, blank=True, to='backend.gleader', null=True),
        ),
    ]
