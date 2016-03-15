# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productions', '0012_productionpagejuicersource'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productionpagejuicersource',
            old_name='source_name',
            new_name='name',
        ),
    ]
