# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0005_auto_20151007_1517'),
    ]

    operations = [
        migrations.AlterField(
            model_name='server',
            name='udid',
            field=models.CharField(max_length=150, null=True, blank=True),
        ),
    ]
