# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Association',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('model', models.CharField(max_length=1, choices=[(b'Project', b'Project'), (b'Paper', b'Paper'), (b'Both', b'Both')])),
            ],
        ),
        migrations.CreateModel(
            name='College',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Paper',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=500)),
                ('stub', models.CharField(unique=True, max_length=5)),
                ('address', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Participant',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('phone', models.BigIntegerField()),
                ('email', models.EmailField(unique=True, max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=500)),
                ('upload', models.FileField(upload_to=b'')),
                ('stub', models.CharField(unique=True, max_length=5)),
                ('assoc', models.ForeignKey(to='registrations.Association')),
                ('category', models.ForeignKey(to='registrations.Category')),
                ('college', models.ForeignKey(to='registrations.College')),
                ('leader', models.ForeignKey(related_name='leaders', to='registrations.Participant')),
                ('members', models.ManyToManyField(related_name='members', to='registrations.Participant')),
            ],
        ),
        migrations.AddField(
            model_name='paper',
            name='author',
            field=models.ForeignKey(related_name='authors', to='registrations.Participant'),
        ),
        migrations.AddField(
            model_name='paper',
            name='category',
            field=models.ForeignKey(to='registrations.Category'),
        ),
        migrations.AddField(
            model_name='paper',
            name='co_author',
            field=models.ForeignKey(related_name='co_authors', to='registrations.Participant'),
        ),
        migrations.AddField(
            model_name='paper',
            name='college',
            field=models.ForeignKey(to='registrations.College'),
        ),
    ]
