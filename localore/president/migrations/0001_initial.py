# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import datetime
import wagtail.wagtailcore.blocks
import wagtail.wagtailimages.blocks
import wagtail.wagtailcore.fields
import blog.models
import wagtail.wagtailembeds.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('localore_admin', '0009_auto_20161026_1333'),
        ('wagtailcore', '0029_unicode_slugfield_dj19'),
    ]

    operations = [
        migrations.CreateModel(
            name='PresidentIndexPage',
            fields=[
                ('page_ptr', models.OneToOneField(serialize=False, to='wagtailcore.Page', primary_key=True, parent_link=True, auto_created=True)),
                ('subtitle', models.CharField(max_length=255, blank=True)),
                ('intro', wagtail.wagtailcore.fields.RichTextField(blank=True)),
                ('share_your_store_text', wagtail.wagtailcore.fields.RichTextField(verbose_name='Share Your Story text')),
                ('social_image', models.ForeignKey(help_text='Optional. The image to use when sharing the page on social networks.', related_name='+', to='localore_admin.LocaloreImage', on_delete=django.db.models.deletion.SET_NULL, blank=True, null=True)),
            ],
            options={
                'verbose_name': 'President Series Index',
            },
            bases=('wagtailcore.page', models.Model),
        ),
        migrations.CreateModel(
            name='PresidentPage',
            fields=[
                ('page_ptr', models.OneToOneField(serialize=False, to='wagtailcore.Page', primary_key=True, parent_link=True, auto_created=True)),
                ('subtitle', models.CharField(max_length=255, blank=True)),
                ('image_credit_caption', wagtail.wagtailcore.fields.RichTextField(verbose_name='credit caption', blank=True)),
                ('intro', wagtail.wagtailcore.fields.StreamField((('heading', wagtail.wagtailcore.blocks.CharBlock(template='blog/blocks/heading.html', icon='title', classname='full title')), ('quote', wagtail.wagtailcore.blocks.StructBlock((('quote', wagtail.wagtailcore.blocks.TextBlock('quote title')), ('attribution', wagtail.wagtailcore.blocks.CharBlock())))), ('paragraph', wagtail.wagtailcore.blocks.RichTextBlock(label='Rich Text', icon='doc-full')), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock(icon='image')), ('embed', wagtail.wagtailembeds.blocks.EmbedBlock(icon='media')), ('caption', blog.models.CaptionBlock()), ('raw_html', wagtail.wagtailcore.blocks.RawHTMLBlock(help_text='<ul class="messages"><li class="error">Please mind that using raw HTML can break site rendering and/or compromise site security.</li></ul>', label='Raw HTML', icon='code'))))),
                ('aired_on_date', models.DateField(default=datetime.date.today)),
                ('body', wagtail.wagtailcore.fields.StreamField((('heading', wagtail.wagtailcore.blocks.CharBlock(template='blog/blocks/heading.html', icon='title', classname='full title')), ('quote', wagtail.wagtailcore.blocks.StructBlock((('quote', wagtail.wagtailcore.blocks.TextBlock('quote title')), ('attribution', wagtail.wagtailcore.blocks.CharBlock())))), ('paragraph', wagtail.wagtailcore.blocks.RichTextBlock(label='Rich Text', icon='doc-full')), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock(icon='image')), ('embed', wagtail.wagtailembeds.blocks.EmbedBlock(icon='media')), ('caption', blog.models.CaptionBlock()), ('raw_html', wagtail.wagtailcore.blocks.RawHTMLBlock(help_text='<ul class="messages"><li class="error">Please mind that using raw HTML can break site rendering and/or compromise site security.</li></ul>', label='Raw HTML', icon='code'))), blank=True)),
                ('hero_image', models.ForeignKey(help_text='The header/hero/feature image for this President Series post.', related_name='+', to='localore_admin.LocaloreImage', on_delete=django.db.models.deletion.SET_NULL, blank=True, null=True)),
                ('social_image', models.ForeignKey(help_text='Optional. The image to use when sharing the page on social networks.', related_name='+', to='localore_admin.LocaloreImage', on_delete=django.db.models.deletion.SET_NULL, blank=True, null=True)),
                ('tile_image', models.ForeignKey(help_text='Optional: The image to use on the President Series index page. Will use hero image if not set.', related_name='+', to='localore_admin.LocaloreImage', on_delete=django.db.models.deletion.SET_NULL, blank=True, null=True)),
            ],
            options={
                'verbose_name': 'President Series Post',
            },
            bases=('wagtailcore.page', models.Model),
        ),
    ]
