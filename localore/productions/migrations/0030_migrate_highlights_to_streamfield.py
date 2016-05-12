# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations
from wagtail.wagtailcore.rich_text import RichText


def convert_to_streamfield(apps, _):
    production_page_model = apps.get_model("productions", "ProductionPage")
    for page in production_page_model.objects.all():
        if page.highlights.raw_text and not page.highlights:
            page.highlights = [
                ('paragraph', RichText(page.highlights.raw_text)),
            ]
            page.save()


def convert_to_richtext(apps, _):
    production_page_model = apps.get_model("productions", "ProductionPage")
    for page in production_page_model.objects.all():
        if page.highlights.raw_text is None:
            raw_text = ''.join([
                child.value.source for child in page.highlights
                if child.block_type == 'paragraph'
            ])
            page.highlights = raw_text
            page.save()


class Migration(migrations.Migration):

    dependencies = [
        ('productions', '0029_auto_20160512_0937'),
    ]

    operations = [
        migrations.RunPython(
            convert_to_streamfield,
            convert_to_richtext,
        ),
    ]
