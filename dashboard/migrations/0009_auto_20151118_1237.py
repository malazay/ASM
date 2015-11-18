# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0008_auto_20151118_1209'),
    ]

    operations = [
        migrations.AddField(
            model_name='server',
            name='webkit_executable',
            field=models.ForeignKey(blank=True, to='dashboard.iOS_WebKit_Debug_Proxy', null=True),
        ),
        migrations.AlterField(
            model_name='server',
            name='appium_executable',
            field=models.ForeignKey(default=0, to='dashboard.Appium_Executable'),
            preserve_default=False,
        ),
    ]
