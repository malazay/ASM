# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0006_auto_20151009_1151'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appium_Executable',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('display_name', models.CharField(default=b'Default Executable', max_length=500)),
                ('installed_by_npm', models.BooleanField(default=True)),
                ('executable_path', models.CharField(default=b'appium', max_length=500)),
                ('node_path', models.CharField(max_length=500, null=True, blank=True)),
                ('creation_date', models.DateTimeField(default=datetime.datetime.now, verbose_name=b'date created')),
            ],
            options={
                'verbose_name': 'Appium Configuration',
                'verbose_name_plural': 'Appium Configurations',
            },
        ),
        migrations.AddField(
            model_name='server',
            name='appium_executable',
            field=models.ForeignKey(default=1, to='dashboard.Appium_Executable'),
            preserve_default=False,
        ),
    ]
