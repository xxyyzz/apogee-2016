# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Event', '0013_auto_20160118_1726'),
    ]

    operations = [
        migrations.CreateModel(
            name='College',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('is_displayed', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Participant',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('aadhaar', models.CharField(default=None, max_length=8, unique=True, null=True, blank=True)),
                ('name', models.CharField(max_length=200)),
                ('gender', models.CharField(max_length=1, choices=[(b'M', b'Male'), (b'F', b'Female')])),
                ('city', models.CharField(max_length=20)),
                ('phone_one', models.BigIntegerField()),
                ('phone_two', models.BigIntegerField(null=True, blank=True)),
                ('email_id', models.EmailField(unique=True, max_length=254)),
                ('email_verified', models.BooleanField(default=False)),
                ('email_token', models.CharField(max_length=32)),
                ('social_link', models.CharField(max_length=300, null=True, blank=True)),
                ('pcr_approval', models.BooleanField(default=False)),
                ('fee_paid', models.BooleanField(default=False)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('bank_ifsc', models.CharField(max_length=11)),
                ('bank_name', models.CharField(max_length=200)),
                ('bank_account_no', models.CharField(max_length=20)),
                ('address', models.TextField(max_length=1000)),
                ('college', models.ForeignKey(to='backend.College')),
                ('events', models.ManyToManyField(to='Event.Event', blank=True)),
            ],
            options={
                'verbose_name_plural': 'Participants',
            },
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('event', models.ForeignKey(to='Event.Event')),
                ('leader', models.ForeignKey(related_name='leader_team', to='backend.Participant')),
                ('members', models.ManyToManyField(to='backend.Participant')),
            ],
        ),
        migrations.AddField(
            model_name='participant',
            name='teams',
            field=models.ManyToManyField(to='backend.Team', blank=True),
        ),
    ]
