# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import aic2016.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AicSubmission',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('problem_statement', models.CharField(choices=[('1', 'Shit1'), ('2', 'Shit2'), ('3', 'Shit3'), ('4', 'Shit4'), ('5', 'Shit5'), ('6', 'Shit6'), ('7', 'Shit7'), ('8', 'Shit8'), ('9', 'Shit9')], max_length=500)),
                ('solution', models.FileField(upload_to=aic2016.models.upload_aic, default=None)),
            ],
        ),
        migrations.CreateModel(
            name='Participant',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('phone', models.BigIntegerField()),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('college', models.CharField(max_length=200)),
                ('yos', models.PositiveSmallIntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='aicsubmission',
            name='leader',
            field=models.ForeignKey(to='aic2016.Participant', related_name='leaders'),
        ),
        migrations.AddField(
            model_name='aicsubmission',
            name='members',
            field=models.ManyToManyField(blank='True', related_name='members', to='aic2016.Participant'),
        ),
    ]
