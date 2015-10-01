# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_server_server_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='server',
            name='full_reset',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='server',
            name='no_reset',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='server',
            name='session_override',
            field=models.BooleanField(default=True),
        ),
    ]
