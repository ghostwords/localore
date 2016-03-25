# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0008_auto_20160324_1029'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutcontactpage',
            name='subtitle',
            field=models.CharField(max_length=255, blank=True),
        ),
        migrations.AddField(
            model_name='aboutmissionpage',
            name='subtitle',
            field=models.CharField(max_length=255, blank=True),
        ),
        migrations.AddField(
            model_name='aboutteampage',
            name='subtitle',
            field=models.CharField(max_length=255, blank=True),
        ),
    ]
