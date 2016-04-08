# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0015_auto_20160402_1209'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='site_intro',
            field=wagtail.wagtailcore.fields.RichTextField(blank=True),
        ),
    ]
