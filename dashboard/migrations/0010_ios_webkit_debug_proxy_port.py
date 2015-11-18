# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0009_auto_20151118_1237'),
    ]

    operations = [
        migrations.AddField(
            model_name='ios_webkit_debug_proxy',
            name='port',
            field=models.CharField(default=b'27753', max_length=5),
        ),
    ]
