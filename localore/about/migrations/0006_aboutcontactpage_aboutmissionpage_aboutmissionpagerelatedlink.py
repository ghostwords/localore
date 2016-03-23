# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import wagtail.wagtailcore.fields
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0028_merge'),
        ('blog', '0016_auto_20160316_1520'),
        ('about', '0005_auto_20160322_1256'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutContactPage',
            fields=[
                ('page_ptr', models.OneToOneField(serialize=False, auto_created=True, parent_link=True, primary_key=True, to='wagtailcore.Page')),
                ('contact_information', wagtail.wagtailcore.fields.RichTextField()),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='AboutMissionPage',
            fields=[
                ('page_ptr', models.OneToOneField(serialize=False, auto_created=True, parent_link=True, primary_key=True, to='wagtailcore.Page')),
                ('description_top', wagtail.wagtailcore.fields.RichTextField()),
                ('description_bottom', wagtail.wagtailcore.fields.RichTextField()),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='AboutMissionPageRelatedLink',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('link_external', models.URLField(blank=True, verbose_name='External link', max_length=500)),
                ('title', models.CharField(help_text='Link title', max_length=255)),
                ('link_page', models.ForeignKey(blank=True, to='blog.BlogPage', related_name='+', null=True)),
                ('page', modelcluster.fields.ParentalKey(related_name='related_links', to='about.AboutMissionPage')),
            ],
            options={
                'abstract': False,
                'ordering': ['sort_order'],
            },
        ),
    ]
