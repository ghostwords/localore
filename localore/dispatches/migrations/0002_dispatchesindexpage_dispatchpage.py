# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
import wagtail.wagtailcore.fields
import localflavor.us.models


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0028_merge'),
        ('dispatches', '0001_squashed_0003_auto_20160402_1324'),
    ]

    operations = [
        migrations.CreateModel(
            name='DispatchesIndexPage',
            fields=[
                ('page_ptr', models.OneToOneField(parent_link=True, primary_key=True, auto_created=True, serialize=False, to='wagtailcore.Page')),
                ('subtitle', models.CharField(max_length=255, blank=True)),
                ('intro', wagtail.wagtailcore.fields.RichTextField(blank=True)),
                ('default_dispatch_type', models.CharField(default='g', max_length=1, choices=[('g', 'Video'), ('l', 'Audio'), ('l', 'Series')])),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='DispatchPage',
            fields=[
                ('page_ptr', models.OneToOneField(parent_link=True, primary_key=True, auto_created=True, serialize=False, to='wagtailcore.Page')),
                ('date', models.DateField(default=datetime.date.today, verbose_name='Post date')),
                ('city', models.CharField(max_length=255)),
                ('state', localflavor.us.models.USStateField(max_length=2, choices=[('AL', 'Alabama'), ('AK', 'Alaska'), ('AS', 'American Samoa'), ('AZ', 'Arizona'), ('AR', 'Arkansas'), ('AA', 'Armed Forces Americas'), ('AE', 'Armed Forces Europe'), ('AP', 'Armed Forces Pacific'), ('CA', 'California'), ('CO', 'Colorado'), ('CT', 'Connecticut'), ('DE', 'Delaware'), ('DC', 'District of Columbia'), ('FL', 'Florida'), ('GA', 'Georgia'), ('GU', 'Guam'), ('HI', 'Hawaii'), ('ID', 'Idaho'), ('IL', 'Illinois'), ('IN', 'Indiana'), ('IA', 'Iowa'), ('KS', 'Kansas'), ('KY', 'Kentucky'), ('LA', 'Louisiana'), ('ME', 'Maine'), ('MD', 'Maryland'), ('MA', 'Massachusetts'), ('MI', 'Michigan'), ('MN', 'Minnesota'), ('MS', 'Mississippi'), ('MO', 'Missouri'), ('MT', 'Montana'), ('NE', 'Nebraska'), ('NV', 'Nevada'), ('NH', 'New Hampshire'), ('NJ', 'New Jersey'), ('NM', 'New Mexico'), ('NY', 'New York'), ('NC', 'North Carolina'), ('ND', 'North Dakota'), ('MP', 'Northern Mariana Islands'), ('OH', 'Ohio'), ('OK', 'Oklahoma'), ('OR', 'Oregon'), ('PA', 'Pennsylvania'), ('PR', 'Puerto Rico'), ('RI', 'Rhode Island'), ('SC', 'South Carolina'), ('SD', 'South Dakota'), ('TN', 'Tennessee'), ('TX', 'Texas'), ('UT', 'Utah'), ('VT', 'Vermont'), ('VI', 'Virgin Islands'), ('VA', 'Virginia'), ('WA', 'Washington'), ('WV', 'West Virginia'), ('WI', 'Wisconsin'), ('WY', 'Wyoming')])),
                ('description', wagtail.wagtailcore.fields.RichTextField(blank=True)),
                ('dispatch_type', models.CharField(default='g', max_length=1, choices=[('g', 'Video'), ('l', 'Audio'), ('l', 'Series')])),
                ('embed_url', models.URLField(verbose_name='URL')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]
