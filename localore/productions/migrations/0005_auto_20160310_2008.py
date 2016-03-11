# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productions', '0004_productionpagerelatedlink_social_site'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productionpagerelatedlink',
            old_name='social_site',
            new_name='site',
        ),
    ]
