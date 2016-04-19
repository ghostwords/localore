# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import wagtail.wagtailembeds.blocks
import wagtail.wagtailcore.blocks
import wagtail.wagtailimages.blocks
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0035_blogpage_video_is_360'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpage',
            name='body',
            field=wagtail.wagtailcore.fields.StreamField((('heading', wagtail.wagtailcore.blocks.CharBlock(classname='full title', icon='title', template='blog/blocks/heading.html')), ('quote', wagtail.wagtailcore.blocks.StructBlock((('quote', wagtail.wagtailcore.blocks.TextBlock('quote title')), ('attribution', wagtail.wagtailcore.blocks.CharBlock())))), ('paragraph', wagtail.wagtailcore.blocks.RichTextBlock(label='Rich Text', icon='doc-full')), ('image_caption', wagtail.wagtailcore.blocks.StructBlock((('image', wagtail.wagtailimages.blocks.ImageChooserBlock(required=True)), ('caption', wagtail.wagtailcore.blocks.RichTextBlock())))), ('embed_caption', wagtail.wagtailcore.blocks.StructBlock((('embed', wagtail.wagtailembeds.blocks.EmbedBlock(required=True)), ('caption', wagtail.wagtailcore.blocks.RichTextBlock())))), ('raw_html', wagtail.wagtailcore.blocks.RawHTMLBlock(label='Raw HTML', help_text='<ul class="messages"><li class="error">Please mind that using raw HTML can break site rendering and/or compromise site security.</li></ul>', icon='code')))),
        ),
    ]
