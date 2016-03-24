# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0017_auto_20160322_1506'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogindexrelatedlink',
            name='link_external',
            field=models.URLField(max_length=500, blank=True, help_text='Please provide an external URL, or select a page below.', verbose_name='External link'),
        ),
        migrations.AlterField(
            model_name='blogindexrelatedlink',
            name='link_page',
            field=models.ForeignKey(blank=True, related_name='+', on_delete=django.db.models.deletion.SET_NULL, to='wagtailcore.Page', verbose_name='Internal link', null=True),
        ),
    ]
