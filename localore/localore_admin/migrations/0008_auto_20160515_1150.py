# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('localore_admin', '0007_auto_20160515_1146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='googleanalytics',
            name='ga_tracking_id',
            field=models.CharField(verbose_name='Google Analytics tracking ID', max_length=20, blank=True),
        ),
        migrations.AlterField(
            model_name='juicersettings',
            name='juicer_auth_token',
            field=models.CharField(max_length=200, help_text='Your Juicer API authentication token.', blank=True),
        ),
        migrations.AlterField(
            model_name='juicersettings',
            name='juicer_feed_id',
            field=models.CharField(max_length=200, help_text='Your Juicer feed ID.', blank=True),
        ),
    ]
