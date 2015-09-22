# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registrations', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'categories'},
        ),
        migrations.AddField(
            model_name='participant',
            name='college',
            field=models.ForeignKey(default=None, to='registrations.College'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='category',
            name='model',
            field=models.CharField(max_length=8, choices=[(b'Project', b'Project'), (b'Paper', b'Paper'), (b'Both', b'Both')]),
        ),
    ]
