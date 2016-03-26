# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('productions', '0020_productionsindexpage_default_view'),
    ]

    operations = [
        migrations.AddField(
            model_name='productionsindexpage',
            name='intro',
            field=wagtail.wagtailcore.fields.RichTextField(blank=True),
        ),
        migrations.AddField(
            model_name='productionsindexpage',
            name='subtitle',
            field=models.CharField(max_length=255, blank=True),
        ),
    ]
