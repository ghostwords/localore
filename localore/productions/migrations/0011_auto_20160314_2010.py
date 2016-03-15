# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('productions', '0010_auto_20160310_2235'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productionpage',
            name='hero_image',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.SET_NULL, help_text='The header/hero/feature image for this production.', related_name='+', null=True, to='wagtailimages.Image'),
        ),
    ]
