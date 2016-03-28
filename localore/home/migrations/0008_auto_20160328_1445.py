# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0028_merge'),
        ('home', '0007_auto_20160328_1425'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='related_content_page',
            field=models.ForeignKey(related_name='+', null=True, to='wagtailcore.Page', blank=True, on_delete=django.db.models.deletion.SET_NULL),
        ),
        migrations.AddField(
            model_name='homepage',
            name='related_content_title',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
