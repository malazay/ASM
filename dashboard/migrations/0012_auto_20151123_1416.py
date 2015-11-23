# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0011_auto_20151118_1305'),
    ]

    operations = [
        migrations.AlterField(
            model_name='server',
            name='bootstrap_port',
            field=models.CharField(max_length=5, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='server',
            name='chromedriver_port',
            field=models.CharField(max_length=5, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='server',
            name='ip_address',
            field=models.CharField(default=b'0.0.0.0', max_length=20),
        ),
        migrations.AlterField(
            model_name='server',
            name='selendroid_port',
            field=models.CharField(max_length=5, null=True, blank=True),
        ),
    ]
