# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0002_person_production'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='biography',
            field=wagtail.wagtailcore.fields.RichTextField(blank=True),
        ),
    ]
