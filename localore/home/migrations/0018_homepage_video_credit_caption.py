# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0017_homepage_video_is_360'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='video_credit_caption',
            field=wagtail.wagtailcore.fields.RichTextField(verbose_name='credit caption', blank=True),
        ),
    ]
