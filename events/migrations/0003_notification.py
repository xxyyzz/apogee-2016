# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_event_is_kernel'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content', ckeditor.fields.RichTextField()),
                ('types', models.CharField(default=b'static', max_length=20, choices=[(b'static', b'static'), (b'internal', b'internal'), (b'external', b'external')])),
                ('link', models.CharField(default=b'None', max_length=50)),
            ],
        ),
    ]
