# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productions', '0015_auto_20160314_2320'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='productionpagerelatedperson',
            options={'ordering': ['sort_order']},
        ),
        migrations.AddField(
            model_name='productionpagerelatedperson',
            name='sort_order',
            field=models.IntegerField(null=True, editable=False, blank=True),
        ),
    ]
