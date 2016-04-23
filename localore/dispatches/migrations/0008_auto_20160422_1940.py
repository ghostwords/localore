# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dispatches', '0007_auto_20160408_1535'),
    ]

    operations = [
        migrations.AddField(
            model_name='dispatchpage',
            name='is_featured',
            field=models.BooleanField(verbose_name='featured', help_text='Makes this dispatch go to the top of the list in its category.', default=False),
        ),
        migrations.AlterField(
            model_name='dispatchpage',
            name='dispatch_type',
            field=models.CharField(choices=[('v', 'Video'), ('a', 'Audio')], verbose_name='category', max_length=1, default='v'),
        ),
    ]
