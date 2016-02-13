# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lacuna', '0007_auto_20160213_1004'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='level',
            name='content',
        ),
        migrations.AddField(
            model_name='level',
            name='css_file',
            field=models.TextField(default=b'NA'),
        ),
        migrations.AddField(
            model_name='level',
            name='html_file',
            field=models.TextField(default=b'NA'),
        ),
        migrations.AddField(
            model_name='level',
            name='js_file',
            field=models.TextField(default=b'NA'),
        ),
    ]
