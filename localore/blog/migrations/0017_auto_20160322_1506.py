# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0016_auto_20160316_1520'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogindexrelatedlink',
            name='link_page',
            field=models.ForeignKey(to='wagtailcore.Page', blank=True, verbose_name='Internal link', null=True, related_name='+'),
        ),
        migrations.AlterField(
            model_name='blogindexrelatedlink',
            name='title',
            field=models.CharField(max_length=255),
        ),
    ]
