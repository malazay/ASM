# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0010_ios_webkit_debug_proxy_port'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ios_webkit_debug_proxy',
            old_name='installed_by_npm',
            new_name='installed_by_brew',
        ),
    ]
