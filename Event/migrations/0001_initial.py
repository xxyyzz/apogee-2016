# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EventCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('weight', models.IntegerField(help_text=b'Heavier items sink to the bottom of the menu.')),
            ],
            options={
                'verbose_name_plural': 'Event Categories',
            },
        ),
        migrations.CreateModel(
            name='events',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=100, verbose_name=b'Event Name')),
                ('overview', models.TextField(blank=b'True')),
                ('contact', models.TextField(blank=b'True')),
                ('content', ckeditor.fields.RichTextField()),
                ('register', models.BooleanField(verbose_name=b'Enable online registration')),
                ('is_team', models.BooleanField(verbose_name=b'Team event')),
                ('max_participants', models.IntegerField(null=True, blank=True)),
                ('weight', models.IntegerField(null=True, blank=True)),
                ('date', models.CharField(max_length=100, blank=True)),
                ('startingtime', models.CharField(max_length=100, blank=True)),
                ('endingtime', models.CharField(max_length=100, blank=True)),
                ('venue', models.CharField(max_length=100, blank=True)),
                ('img', models.ImageField(upload_to=b'imageuploads', blank=True)),
                ('thumb', models.ImageField(upload_to=b'imageuploads', blank=True)),
                ('is_kernel', models.NullBooleanField()),
                ('category', models.ForeignKey(to='Event.EventCategory')),
            ],
        ),
        migrations.CreateModel(
            name='Heading',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=60)),
                ('weight', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Tab heading',
                'verbose_name_plural': 'Tab headings',
            },
        ),
        migrations.CreateModel(
            name='Tabs',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content', models.TextField(blank=True)),
                ('event', models.ForeignKey(to='Event.events')),
                ('heading', models.ForeignKey(to='Event.Heading')),
            ],
            options={
                'verbose_name': 'Tab',
                'verbose_name_plural': 'Tabs',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=15)),
            ],
        ),
        migrations.AddField(
            model_name='events',
            name='tag',
            field=models.ManyToManyField(to='Event.Tag', blank=True),
        ),
    ]
