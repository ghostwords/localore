# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import localflavor.us.models
import django.db.models.deletion
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0023_alter_page_revision_on_delete_behaviour'),
        ('wagtailimages', '0010_change_on_delete_behaviour'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductionPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, parent_link=True, primary_key=True, to='wagtailcore.Page', serialize=False)),
                ('city', models.CharField(max_length=255)),
                ('state', localflavor.us.models.USStateField(max_length=2, choices=[('AL', 'Alabama'), ('AK', 'Alaska'), ('AS', 'American Samoa'), ('AZ', 'Arizona'), ('AR', 'Arkansas'), ('AA', 'Armed Forces Americas'), ('AE', 'Armed Forces Europe'), ('AP', 'Armed Forces Pacific'), ('CA', 'California'), ('CO', 'Colorado'), ('CT', 'Connecticut'), ('DE', 'Delaware'), ('DC', 'District of Columbia'), ('FL', 'Florida'), ('GA', 'Georgia'), ('GU', 'Guam'), ('HI', 'Hawaii'), ('ID', 'Idaho'), ('IL', 'Illinois'), ('IN', 'Indiana'), ('IA', 'Iowa'), ('KS', 'Kansas'), ('KY', 'Kentucky'), ('LA', 'Louisiana'), ('ME', 'Maine'), ('MD', 'Maryland'), ('MA', 'Massachusetts'), ('MI', 'Michigan'), ('MN', 'Minnesota'), ('MS', 'Mississippi'), ('MO', 'Missouri'), ('MT', 'Montana'), ('NE', 'Nebraska'), ('NV', 'Nevada'), ('NH', 'New Hampshire'), ('NJ', 'New Jersey'), ('NM', 'New Mexico'), ('NY', 'New York'), ('NC', 'North Carolina'), ('ND', 'North Dakota'), ('MP', 'Northern Mariana Islands'), ('OH', 'Ohio'), ('OK', 'Oklahoma'), ('OR', 'Oregon'), ('PA', 'Pennsylvania'), ('PR', 'Puerto Rico'), ('RI', 'Rhode Island'), ('SC', 'South Carolina'), ('SD', 'South Dakota'), ('TN', 'Tennessee'), ('TX', 'Texas'), ('UT', 'Utah'), ('VT', 'Vermont'), ('VI', 'Virgin Islands'), ('VA', 'Virginia'), ('WA', 'Washington'), ('WV', 'West Virginia'), ('WI', 'Wisconsin'), ('WY', 'Wyoming')])),
                ('description', wagtail.wagtailcore.fields.RichTextField()),
                ('twitter_url', models.URLField(blank=True, verbose_name='Twitter URL')),
                ('instagram_url', models.URLField(blank=True, verbose_name='Instagram URL')),
                ('youtube_url', models.URLField(blank=True, verbose_name='YouTube URL')),
                ('tumblr_url', models.URLField(blank=True, verbose_name='Tumblr URL')),
                ('soundcloud_url', models.URLField(blank=True, verbose_name='SoundCloud URL')),
                ('vine_url', models.URLField(blank=True, verbose_name='Vine URL')),
                ('highlights', wagtail.wagtailcore.fields.RichTextField(blank=True, help_text="Optional WYSIWYG area to highlight the production's work.")),
                ('hero_image', models.ForeignKey(null=True, help_text='The large header/feature/hero image for this production.', on_delete=django.db.models.deletion.SET_NULL, to='wagtailimages.Image', related_name='+')),
                ('logo_image', models.ForeignKey(null=True, blank=True, help_text="The production's logo (optional).", on_delete=django.db.models.deletion.SET_NULL, to='wagtailimages.Image', related_name='+')),
            ],
            options={
                'verbose_name': 'production',
            },
            bases=('wagtailcore.page',),
        ),
    ]
