# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_server_command_timeout'),
    ]

    operations = [
        migrations.AddField(
            model_name='server',
            name='udid',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='server',
            name='command_timeout',
            field=models.IntegerField(default=120),
        ),
    ]
