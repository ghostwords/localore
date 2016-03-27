# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('localore_admin', '0002_auto_20160316_1444'),
    ]

    run_before = [
        ('home', '0002_create_homepage'),
        ('people', '0006_auto_20160318_1718'),
    ]

    operations = [
        migrations.RenameField(
            model_name='localoreimage',
            old_name='alt',
            new_name='alt_text',
        ),
    ]
