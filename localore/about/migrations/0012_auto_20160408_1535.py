# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0011_auto_20160331_1015'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='aboutcontactpage',
            options={'verbose_name': 'About: Connect'},
        ),
        migrations.AlterModelOptions(
            name='aboutmissionpage',
            options={'verbose_name': 'About: Mission'},
        ),
        migrations.AlterModelOptions(
            name='aboutteampage',
            options={'verbose_name': 'About: Team'},
        ),
    ]
