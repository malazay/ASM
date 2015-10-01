# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_auto_20151001_1358'),
    ]

    operations = [
        migrations.AddField(
            model_name='server',
            name='command_timeout',
            field=models.IntegerField(default=120, max_length=3),
        ),
    ]
