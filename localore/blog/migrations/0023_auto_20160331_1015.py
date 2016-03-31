# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0022_blogpage_subtitle'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogindexrelatedlink',
            name='link_external',
            field=models.CharField(help_text='Please provide an external URL, or select a page below.', verbose_name='External link', max_length=500, blank=True),
        ),
    ]
