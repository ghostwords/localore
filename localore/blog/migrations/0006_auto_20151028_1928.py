# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import wagtail.wagtailcore.fields
import wagtail.wagtailimages.blocks
import wagtail.wagtailcore.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20151028_1845'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpage',
            name='body',
            field=wagtail.wagtailcore.fields.StreamField((('heading', wagtail.wagtailcore.blocks.CharBlock(classname='full title')), ('paragraph', wagtail.wagtailcore.blocks.RichTextBlock(label='Rich Text', icon='doc-full')), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('html', wagtail.wagtailcore.blocks.RawHTMLBlock(label='HTML', icon='site')))),
        ),
    ]
