# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('Event', '0006_auto_20151224_1809'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tabs',
            name='content',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
