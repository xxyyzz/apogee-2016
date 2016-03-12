# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Results',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('roll_no', models.IntegerField()),
                ('standard', models.CharField(max_length=10)),
                ('national_rank', models.IntegerField()),
                ('school_rank', models.IntegerField()),
            ],
        ),
    ]
