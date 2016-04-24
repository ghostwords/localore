# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0038_auto_20160420_1348'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpage',
            name='video_credit_caption',
            field=wagtail.wagtailcore.fields.RichTextField(verbose_name='credit caption', blank=True),
        ),
    ]
