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
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('solution', models.FileField(upload_to=iot.models.upload_iot, default=None)),
            ],
        ),
        migrations.CreateModel(
            name='Participant',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
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
            field=models.ForeignKey(related_name='leaders', to='iot.Participant'),
        ),
        migrations.AddField(
            model_name='iotsubmission',
            name='members',
            field=models.ManyToManyField(to='iot.Participant', related_name='members', blank='True'),
        ),
    ]
