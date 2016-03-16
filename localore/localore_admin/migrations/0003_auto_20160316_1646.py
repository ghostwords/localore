# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('localore_admin', '0002_auto_20160316_1444'),
    ]

    operations = [
        migrations.RenameField(
            model_name='localoreimage',
            old_name='alt',
            new_name='alt_text',
        ),
    ]
