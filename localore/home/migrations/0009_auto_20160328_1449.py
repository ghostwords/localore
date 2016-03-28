# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_auto_20160328_1445'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='homepage',
            name='subtitle',
        ),
        migrations.AddField(
            model_name='homepage',
            name='related_content_subtitle',
            field=models.CharField(default='Across America', verbose_name='subtitle', max_length=255, blank=True),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='related_content_page',
            field=models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, related_name='+', verbose_name='page', blank=True, null=True, to='wagtailcore.Page'),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='related_content_title',
            field=models.CharField(blank=True, max_length=255, verbose_name='title'),
        ),
    ]
