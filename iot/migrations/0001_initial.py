# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import iot.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='IotSubmission',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('problem_statement', models.CharField(choices=[('1', 'Shit1'), ('2', 'Shit2'), ('3', 'Shit3'), ('4', 'Shit4'), ('5', 'Shit5'), ('6', 'Shit6'), ('7', 'Shit7'), ('8', 'Shit8'), ('9', 'Shit9')], max_length=500)),
                ('solution', models.FileField(upload_to=iot.models.upload_iot, default=None)),
            ],
        ),
        migrations.CreateModel(
            name='Participant',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=200)),
                ('phone', models.BigIntegerField()),
                ('email', models.EmailField(unique=True, max_length=254)),
                ('college', models.CharField(max_length=200)),
                ('yos', models.PositiveSmallIntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='iotsubmission',
            name='leader',
            field=models.ForeignKey(to='iot.Participant', related_name='leaders'),
        ),
        migrations.AddField(
            model_name='iotsubmission',
            name='members',
            field=models.ManyToManyField(to='iot.Participant', related_name='members', blank='True'),
        ),
    ]
