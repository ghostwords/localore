# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import wagtail.wagtailcore.fields
import wagtail.wagtailimages.blocks
import wagtail.wagtailcore.blocks
import blog.models
import wagtail.wagtailembeds.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('productions', '0028_productionpage_host_station_call_sign'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productionpage',
            name='highlights',
            field=wagtail.wagtailcore.fields.StreamField((('heading', wagtail.wagtailcore.blocks.CharBlock(icon='title', template='blog/blocks/heading.html', classname='full title')), ('quote', wagtail.wagtailcore.blocks.StructBlock((('quote', wagtail.wagtailcore.blocks.TextBlock('quote title')), ('attribution', wagtail.wagtailcore.blocks.CharBlock())))), ('paragraph', wagtail.wagtailcore.blocks.RichTextBlock(label='Rich Text', icon='doc-full')), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock(icon='image')), ('embed', wagtail.wagtailembeds.blocks.EmbedBlock(icon='media')), ('caption', blog.models.CaptionBlock()), ('raw_html', wagtail.wagtailcore.blocks.RawHTMLBlock(label='Raw HTML', help_text='<ul class="messages"><li class="error">Please mind that using raw HTML can break site rendering and/or compromise site security.</li></ul>', icon='code'))), blank=True),
        ),
    ]
