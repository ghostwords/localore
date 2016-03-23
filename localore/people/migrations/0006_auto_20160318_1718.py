# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0005_auto_20160316_1520'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='person',
            options={'verbose_name': 'person', 'verbose_name_plural': 'people', 'ordering': ('first_name', 'last_name')},
        ),
        migrations.RemoveField(
            model_name='person',
            name='production',
        ),
    ]
