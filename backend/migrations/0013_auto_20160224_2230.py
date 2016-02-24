# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0012_merge'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participant',
            name='bill_id',
            field=models.CharField(blank=True, default='', max_length=10),
        ),
        migrations.AlterField(
            model_name='participant',
            name='controlz',
            field=models.BooleanField(verbose_name='passed controlz', default=False),
        ),
        migrations.AlterField(
            model_name='participant',
            name='firewallzo',
            field=models.BooleanField(verbose_name='passed firewallz', default=False),
        ),
        migrations.AlterField(
            model_name='participant',
            name='recnacc',
            field=models.BooleanField(verbose_name='passed recnacc', default=False),
        ),
    ]
