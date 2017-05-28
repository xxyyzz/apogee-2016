# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Event', '0044_auto_20160218_0020'),
        ('ems', '0003_auto_20160217_2315'),
    ]

    operations = [
        migrations.AddField(
            model_name='label',
            name='event',
            field=models.ForeignKey(default=1, to='Event.Event'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='label',
            name='var10name',
            field=models.CharField(max_length=100, blank=True),
        ),
        migrations.AlterField(
            model_name='label',
            name='var1name',
            field=models.CharField(max_length=100, blank=True),
        ),
        migrations.AlterField(
            model_name='label',
            name='var2name',
            field=models.CharField(max_length=100, blank=True),
        ),
        migrations.AlterField(
            model_name='label',
            name='var3name',
            field=models.CharField(max_length=100, blank=True),
        ),
        migrations.AlterField(
            model_name='label',
            name='var4name',
            field=models.CharField(max_length=100, blank=True),
        ),
        migrations.AlterField(
            model_name='label',
            name='var5name',
            field=models.CharField(max_length=100, blank=True),
        ),
        migrations.AlterField(
            model_name='label',
            name='var6name',
            field=models.CharField(max_length=100, blank=True),
        ),
        migrations.AlterField(
            model_name='label',
            name='var7name',
            field=models.CharField(max_length=100, blank=True),
        ),
        migrations.AlterField(
            model_name='label',
            name='var8name',
            field=models.CharField(max_length=100, blank=True),
        ),
        migrations.AlterField(
            model_name='label',
            name='var9name',
            field=models.CharField(max_length=100, blank=True),
        ),
    ]
