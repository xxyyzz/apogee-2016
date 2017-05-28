# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registrations', '0009_auto_20151123_2158'),
    ]

    operations = [
        migrations.CreateModel(
            name='InitialRegistration',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone', models.BigIntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='category',
            name='model',
            field=models.CharField(choices=[('Project', 'Project'), ('Paper', 'Paper'), ('Both', 'Both')], max_length=8),
        ),
        migrations.AlterField(
            model_name='paper',
            name='status',
            field=models.CharField(choices=[('0', 'Submitted'), ('1', 'Passed Round 1'), ('2', 'Passed Round 2')], max_length=2, default='0'),
        ),
        migrations.AlterField(
            model_name='project',
            name='status',
            field=models.CharField(choices=[('0', 'Submitted'), ('1', 'Passed Round 1'), ('2', 'Passed Round 2')], max_length=2, default='0'),
        ),
    ]
