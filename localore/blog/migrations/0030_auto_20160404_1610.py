# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import wagtail.wagtailcore.fields
import wagtail.wagtailcore.blocks
import wagtail.wagtailembeds.blocks
import wagtail.wagtailimages.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0029_auto_20160404_1553'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpage',
            name='body',
            field=wagtail.wagtailcore.fields.StreamField((('heading', wagtail.wagtailcore.blocks.CharBlock(template='blog/blocks/heading.html', classname='full title', icon='title')), ('quote', wagtail.wagtailcore.blocks.StructBlock((('quote', wagtail.wagtailcore.blocks.TextBlock('quote title')), ('attribution', wagtail.wagtailcore.blocks.CharBlock())))), ('paragraph', wagtail.wagtailcore.blocks.RichTextBlock(label='Rich Text', icon='doc-full')), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock(icon='image')), ('embed', wagtail.wagtailembeds.blocks.EmbedBlock(icon='media')), ('raw_html', wagtail.wagtailcore.blocks.RawHTMLBlock(label='Raw HTML', help_text='<ul class="messages"><li class="error">Please mind that using raw HTML can break site rendering and/or compromise site security.</li></ul>', icon='code')))),
        ),
    ]
