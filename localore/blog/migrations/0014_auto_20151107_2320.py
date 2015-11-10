# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_auto_20151107_2318'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blogindexpage',
            old_name='intro',
            new_name='body',
        ),
    ]
