# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import wagtail.wagtailcore.fields
import wagtail.wagtailembeds.blocks
import wagtail.wagtailcore.blocks
import wagtail.wagtailimages.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0028_auto_20160402_1209'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpage',
            name='body',
            field=wagtail.wagtailcore.fields.StreamField((('heading', wagtail.wagtailcore.blocks.CharBlock(template='blog/blocks/heading.html', icon='title', classname='full title')), ('quote', wagtail.wagtailcore.blocks.StructBlock((('quote', wagtail.wagtailcore.blocks.TextBlock('quote title')), ('attribution', wagtail.wagtailcore.blocks.CharBlock())))), ('paragraph', wagtail.wagtailcore.blocks.RichTextBlock(icon='doc-full', label='Rich Text')), ('raw_html', wagtail.wagtailcore.blocks.RawHTMLBlock(icon='code', label='Raw HTML')), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock(icon='image')), ('embed', wagtail.wagtailembeds.blocks.EmbedBlock(icon='media')))),
        ),
    ]
