from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('regsoft', '0001_initial'),
        ('backend', '0006_auto_20160212_1427'),
    ]

    operations = [
        migrations.AddField(
            model_name='participant',
            name='controlz',
            field=models.BooleanField(default=False, verbose_name=b'passed controlz'),
        ),
        migrations.AddField(
            model_name='participant',
            name='firewallzo',
            field=models.BooleanField(default=False, verbose_name=b'passed firewallz'),
        ),
        migrations.AddField(
            model_name='participant',
            name='recnacc',
            field=models.BooleanField(default=False, verbose_name=b'passed recnacc'),
        ),
        migrations.AddField(
            model_name='participant',
            name='room',
            field=models.ForeignKey(blank=True, to='regsoft.Room', null=True),
        ),
    ]
