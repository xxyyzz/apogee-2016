# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lacuna', '0003_auto_20160212_1821'),
    ]

    operations = [
        migrations.CreateModel(
            name='Level',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('dept', models.CharField(max_length=10, choices=[(b'DVM', b'DVM'), (b'INFORMALS', b'INFORMALS')])),
                ('level', models.PositiveSmallIntegerField()),
                ('content', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='lacuna',
            name='informals_1',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='lacuna',
            name='informals_10',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='lacuna',
            name='informals_11',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='lacuna',
            name='informals_12',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='lacuna',
            name='informals_2',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='lacuna',
            name='informals_3',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='lacuna',
            name='informals_4',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='lacuna',
            name='informals_5',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='lacuna',
            name='informals_6',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='lacuna',
            name='informals_7',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='lacuna',
            name='informals_8',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='lacuna',
            name='informals_9',
            field=models.PositiveSmallIntegerField(default=0),
        ),
    ]
