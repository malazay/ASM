# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Server',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('server_name', models.CharField(default=b'Server Name', max_length=50)),
                ('ip_address', models.CharField(default=b'127.0.0.1', max_length=20)),
                ('port_number', models.CharField(max_length=5)),
                ('chromedriver_port', models.CharField(max_length=5)),
                ('bootstrap_port', models.CharField(max_length=5)),
                ('selendroid_port', models.CharField(max_length=5)),
                ('creation_date', models.DateTimeField(default=datetime.datetime.now, verbose_name=b'date created')),
            ],
        ),
    ]
