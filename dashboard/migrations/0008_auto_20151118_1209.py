# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0007_auto_20151012_1551'),
    ]

    operations = [
        migrations.CreateModel(
            name='iOS_WebKit_Debug_Proxy',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('display_name', models.CharField(default=b'iOS WebKit Debug Proxy Name', max_length=50)),
                ('installed_by_npm', models.BooleanField(default=True)),
                ('executable_path', models.CharField(default=b'appium', max_length=500)),
                ('node_path', models.CharField(max_length=500, null=True, blank=True)),
                ('creation_date', models.DateTimeField(default=datetime.datetime.now, verbose_name=b'date created')),
            ],
            options={
                'verbose_name': 'iOS WebKit Debug Proxy Configuration',
                'verbose_name_plural': 'iOS WebKit Debug Proxy Configurations',
            },
        ),
        migrations.AddField(
            model_name='server',
            name='is_iOS',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='server',
            name='is_iOS_Simulator',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='server',
            name='appium_executable',
            field=models.ForeignKey(blank=True, to='dashboard.iOS_WebKit_Debug_Proxy', null=True),
        ),
    ]
