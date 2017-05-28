# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Event', '0008_auto_20151228_2036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventcategory',
            name='weight',
            field=models.IntegerField(help_text='Heavier items sink to the bottom of the menu.'),
        ),
        migrations.AlterField(
            model_name='events',
            name='img',
            field=models.ImageField(blank=True, upload_to='imageuploads'),
        ),
        migrations.AlterField(
            model_name='events',
            name='is_team',
            field=models.BooleanField(verbose_name='Team event'),
        ),
        migrations.AlterField(
            model_name='events',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Event Name', unique=True),
        ),
        migrations.AlterField(
            model_name='events',
            name='register',
            field=models.BooleanField(verbose_name='Enable online registration'),
        ),
        migrations.AlterField(
            model_name='events',
            name='thumb',
            field=models.ImageField(blank=True, upload_to='imageuploads'),
        ),
    ]
