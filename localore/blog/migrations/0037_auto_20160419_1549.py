# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import wagtail.wagtailcore.blocks
import wagtail.wagtailimages.blocks
import wagtail.wagtailcore.fields
import wagtail.wagtailembeds.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0036_auto_20160419_1548'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpage',
            name='body',
            field=wagtail.wagtailcore.fields.StreamField((('heading', wagtail.wagtailcore.blocks.CharBlock(icon='title', classname='full title', template='blog/blocks/heading.html')), ('quote', wagtail.wagtailcore.blocks.StructBlock((('quote', wagtail.wagtailcore.blocks.TextBlock('quote title')), ('attribution', wagtail.wagtailcore.blocks.CharBlock())))), ('paragraph', wagtail.wagtailcore.blocks.RichTextBlock(icon='doc-full', label='Rich Text')), ('image_caption', wagtail.wagtailcore.blocks.StructBlock((('image', wagtail.wagtailimages.blocks.ImageChooserBlock(required=True)), ('caption', wagtail.wagtailcore.blocks.RichTextBlock(required=False))))), ('embed_caption', wagtail.wagtailcore.blocks.StructBlock((('embed', wagtail.wagtailembeds.blocks.EmbedBlock(required=True)), ('caption', wagtail.wagtailcore.blocks.RichTextBlock(required=False))))), ('raw_html', wagtail.wagtailcore.blocks.RawHTMLBlock(icon='code', label='Raw HTML', help_text='<ul class="messages"><li class="error">Please mind that using raw HTML can break site rendering and/or compromise site security.</li></ul>')))),
        ),
    ]
