# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('productions', '0019_productionpagefeaturedperson'),
        ('blog', '0019_auto_20160325_1159'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPageAssociatedProduction',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('sort_order', models.IntegerField(editable=False, null=True, blank=True)),
                ('page', modelcluster.fields.ParentalKey(to='blog.BlogPage', related_name='associated_productions')),
                ('production_page', models.ForeignKey(to='productions.ProductionPage', related_name='+')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='BlogPageRelatedConnection',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('sort_order', models.IntegerField(editable=False, null=True, blank=True)),
                ('page', modelcluster.fields.ParentalKey(to='blog.BlogPage', related_name='related_posts')),
                ('related_blog_page', models.ForeignKey(to='blog.BlogPage', verbose_name='Related Connection', related_name='+')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
    ]
