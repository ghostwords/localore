# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0028_merge'),
        ('home', '0012_homepage_video_youtube_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='view_more_page',
            field=models.ForeignKey(related_name='+', to='wagtailcore.Page', null=True, on_delete=django.db.models.deletion.SET_NULL),
        ),
        migrations.AddField(
            model_name='homepage',
            name='view_more_title',
            field=models.CharField(max_length=255, default=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='homepage',
            name='related_content_page',
            field=models.ForeignKey(verbose_name='page to link to', blank=True, to='wagtailcore.Page', related_name='+', null=True, on_delete=django.db.models.deletion.SET_NULL),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='video_youtube_id',
            field=models.CharField(verbose_name='YouTube video ID', max_length=12, help_text='The part in bold: https://www.youtube.com/watch?v=<b>j6IIjLK-8fU</b>', default='j6IIjLK-8fU'),
        ),
    ]
