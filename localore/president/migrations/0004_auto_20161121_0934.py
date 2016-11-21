# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('president', '0003_auto_20161121_0926'),
    ]

    operations = [
        migrations.AlterField(
            model_name='presidentpage',
            name='image_credit_caption',
            field=wagtail.wagtailcore.fields.RichTextField(help_text='Optional: Goes under the hero image.', blank=True, verbose_name='credit caption'),
        ),
        migrations.AlterField(
            model_name='presidentpage',
            name='tile_image',
            field=models.ForeignKey(help_text='The image to use on the President Series index page.', to='localore_admin.LocaloreImage', null=True, blank=True, related_name='+', on_delete=django.db.models.deletion.SET_NULL),
        ),
    ]
