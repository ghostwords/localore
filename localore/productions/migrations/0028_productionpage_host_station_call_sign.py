# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productions', '0027_productionpage_image_credit_caption'),
    ]

    operations = [
        migrations.AddField(
            model_name='productionpage',
            name='host_station_call_sign',
            field=models.CharField(verbose_name='call sign', default='', help_text="The host radio station's call sign.", max_length=12),
            preserve_default=False,
        ),
    ]
