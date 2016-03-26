# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import datetime
import wagtail.wagtailcore.fields
import localflavor.us.models


class Migration(migrations.Migration):

    dependencies = [
        ('localore_admin', '0004_pagealias'),
        ('wagtailcore', '0028_merge'),
    ]

    operations = [
        migrations.CreateModel(
            name='AudioDispatchesIndexPage',
            fields=[
                ('page_ptr', models.OneToOneField(to='wagtailcore.Page', auto_created=True, serialize=False, parent_link=True, primary_key=True)),
                ('subtitle', models.CharField(blank=True, max_length=255)),
                ('intro', wagtail.wagtailcore.fields.RichTextField(blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='AudioDispatchPage',
            fields=[
                ('page_ptr', models.OneToOneField(to='wagtailcore.Page', auto_created=True, serialize=False, parent_link=True, primary_key=True)),
                ('date', models.DateField(verbose_name='Post date', default=datetime.date.today)),
                ('city', models.CharField(max_length=255)),
                ('state', localflavor.us.models.USStateField(max_length=2, choices=[('AL', 'Alabama'), ('AK', 'Alaska'), ('AS', 'American Samoa'), ('AZ', 'Arizona'), ('AR', 'Arkansas'), ('AA', 'Armed Forces Americas'), ('AE', 'Armed Forces Europe'), ('AP', 'Armed Forces Pacific'), ('CA', 'California'), ('CO', 'Colorado'), ('CT', 'Connecticut'), ('DE', 'Delaware'), ('DC', 'District of Columbia'), ('FL', 'Florida'), ('GA', 'Georgia'), ('GU', 'Guam'), ('HI', 'Hawaii'), ('ID', 'Idaho'), ('IL', 'Illinois'), ('IN', 'Indiana'), ('IA', 'Iowa'), ('KS', 'Kansas'), ('KY', 'Kentucky'), ('LA', 'Louisiana'), ('ME', 'Maine'), ('MD', 'Maryland'), ('MA', 'Massachusetts'), ('MI', 'Michigan'), ('MN', 'Minnesota'), ('MS', 'Mississippi'), ('MO', 'Missouri'), ('MT', 'Montana'), ('NE', 'Nebraska'), ('NV', 'Nevada'), ('NH', 'New Hampshire'), ('NJ', 'New Jersey'), ('NM', 'New Mexico'), ('NY', 'New York'), ('NC', 'North Carolina'), ('ND', 'North Dakota'), ('MP', 'Northern Mariana Islands'), ('OH', 'Ohio'), ('OK', 'Oklahoma'), ('OR', 'Oregon'), ('PA', 'Pennsylvania'), ('PR', 'Puerto Rico'), ('RI', 'Rhode Island'), ('SC', 'South Carolina'), ('SD', 'South Dakota'), ('TN', 'Tennessee'), ('TX', 'Texas'), ('UT', 'Utah'), ('VT', 'Vermont'), ('VI', 'Virgin Islands'), ('VA', 'Virginia'), ('WA', 'Washington'), ('WV', 'West Virginia'), ('WI', 'Wisconsin'), ('WY', 'Wyoming')])),
                ('description', wagtail.wagtailcore.fields.RichTextField(blank=True)),
            ],
            options={
                'verbose_name': 'audio dispatch',
                'verbose_name_plural': 'audio dispatches',
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='VideoDispatchesIndexPage',
            fields=[
                ('page_ptr', models.OneToOneField(to='wagtailcore.Page', auto_created=True, serialize=False, parent_link=True, primary_key=True)),
                ('subtitle', models.CharField(blank=True, max_length=255)),
                ('intro', wagtail.wagtailcore.fields.RichTextField(blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='VideoDispatchPage',
            fields=[
                ('page_ptr', models.OneToOneField(to='wagtailcore.Page', auto_created=True, serialize=False, parent_link=True, primary_key=True)),
                ('date', models.DateField(verbose_name='Post date', default=datetime.date.today)),
                ('city', models.CharField(max_length=255)),
                ('state', localflavor.us.models.USStateField(max_length=2, choices=[('AL', 'Alabama'), ('AK', 'Alaska'), ('AS', 'American Samoa'), ('AZ', 'Arizona'), ('AR', 'Arkansas'), ('AA', 'Armed Forces Americas'), ('AE', 'Armed Forces Europe'), ('AP', 'Armed Forces Pacific'), ('CA', 'California'), ('CO', 'Colorado'), ('CT', 'Connecticut'), ('DE', 'Delaware'), ('DC', 'District of Columbia'), ('FL', 'Florida'), ('GA', 'Georgia'), ('GU', 'Guam'), ('HI', 'Hawaii'), ('ID', 'Idaho'), ('IL', 'Illinois'), ('IN', 'Indiana'), ('IA', 'Iowa'), ('KS', 'Kansas'), ('KY', 'Kentucky'), ('LA', 'Louisiana'), ('ME', 'Maine'), ('MD', 'Maryland'), ('MA', 'Massachusetts'), ('MI', 'Michigan'), ('MN', 'Minnesota'), ('MS', 'Mississippi'), ('MO', 'Missouri'), ('MT', 'Montana'), ('NE', 'Nebraska'), ('NV', 'Nevada'), ('NH', 'New Hampshire'), ('NJ', 'New Jersey'), ('NM', 'New Mexico'), ('NY', 'New York'), ('NC', 'North Carolina'), ('ND', 'North Dakota'), ('MP', 'Northern Mariana Islands'), ('OH', 'Ohio'), ('OK', 'Oklahoma'), ('OR', 'Oregon'), ('PA', 'Pennsylvania'), ('PR', 'Puerto Rico'), ('RI', 'Rhode Island'), ('SC', 'South Carolina'), ('SD', 'South Dakota'), ('TN', 'Tennessee'), ('TX', 'Texas'), ('UT', 'Utah'), ('VT', 'Vermont'), ('VI', 'Virgin Islands'), ('VA', 'Virginia'), ('WA', 'Washington'), ('WV', 'West Virginia'), ('WI', 'Wisconsin'), ('WY', 'Wyoming')])),
                ('description', wagtail.wagtailcore.fields.RichTextField(blank=True)),
                ('thumbnail', models.ForeignKey(blank=True, related_name='+', to='localore_admin.LocaloreImage', null=True, on_delete=django.db.models.deletion.SET_NULL)),
            ],
            options={
                'verbose_name': 'video dispatch',
                'verbose_name_plural': 'video dispatches',
            },
            bases=('wagtailcore.page',),
        ),
    ]
