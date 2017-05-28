# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Event', '0017_auto_20160212_0807'),
        ('backend', '0005_auto_20160212_0807'),
    ]

    operations = [
        migrations.CreateModel(
            name='Judge',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Label',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('var1name', models.CharField(max_length=100)),
                ('var1max', models.PositiveSmallIntegerField(default=10)),
                ('var2name', models.CharField(max_length=100)),
                ('var2max', models.PositiveSmallIntegerField(default=10)),
                ('var3name', models.CharField(max_length=100)),
                ('var3max', models.PositiveSmallIntegerField(default=10)),
                ('var4name', models.CharField(max_length=100)),
                ('var4max', models.PositiveSmallIntegerField(default=10)),
                ('var5name', models.CharField(max_length=100)),
                ('var5max', models.PositiveSmallIntegerField(default=10)),
                ('var6name', models.CharField(max_length=100)),
                ('var6max', models.PositiveSmallIntegerField(default=10)),
                ('var7name', models.CharField(max_length=100)),
                ('var7max', models.PositiveSmallIntegerField(default=10)),
                ('var8name', models.CharField(max_length=100)),
                ('var8max', models.PositiveSmallIntegerField(default=10)),
                ('var9name', models.CharField(max_length=100)),
                ('var9max', models.PositiveSmallIntegerField(default=10)),
                ('var10name', models.CharField(max_length=100)),
                ('var10max', models.PositiveSmallIntegerField(default=10)),
            ],
        ),
        migrations.CreateModel(
            name='Level',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('position', models.PositiveSmallIntegerField()),
                ('event', models.ForeignKey(to='Event.Event')),
                ('judges', models.ManyToManyField(to='ems.Judge')),
                ('label', models.ForeignKey(to='ems.Label')),
                ('teams', models.ManyToManyField(related_name='levels', to='backend.Team')),
            ],
        ),
        migrations.CreateModel(
            name='Score',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('var1', models.PositiveSmallIntegerField(default=None, null=True, blank=True)),
                ('var2', models.PositiveSmallIntegerField(default=None, null=True, blank=True)),
                ('var3', models.PositiveSmallIntegerField(default=None, null=True, blank=True)),
                ('var4', models.PositiveSmallIntegerField(default=None, null=True, blank=True)),
                ('var5', models.PositiveSmallIntegerField(default=None, null=True, blank=True)),
                ('var6', models.PositiveSmallIntegerField(default=None, null=True, blank=True)),
                ('var7', models.PositiveSmallIntegerField(default=None, null=True, blank=True)),
                ('var8', models.PositiveSmallIntegerField(default=None, null=True, blank=True)),
                ('var9', models.PositiveSmallIntegerField(default=None, null=True, blank=True)),
                ('var10', models.PositiveSmallIntegerField(default=None, null=True, blank=True)),
                ('judge', models.ForeignKey(to='ems.Judge')),
                ('level', models.ForeignKey(to='ems.Level')),
                ('team', models.ForeignKey(to='backend.Team')),
            ],
        ),
    ]
