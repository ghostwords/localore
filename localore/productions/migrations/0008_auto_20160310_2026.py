# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productions', '0007_auto_20160310_2025'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productionpagerelatedlink',
            old_name='site',
            new_name='service_name',
        ),
    ]
