# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import wagtail.wagtailcore.fields
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0028_merge'),
        ('localore_admin', '0008_auto_20160515_1150'),
        ('home', '0021_homepage_social_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='LiveFeedPage',
            fields=[
                ('page_ptr', models.OneToOneField(serialize=False, parent_link=True, to='wagtailcore.Page', auto_created=True, primary_key=True)),
                ('live_feed_intro', wagtail.wagtailcore.fields.RichTextField(blank=True)),
                ('social_image', models.ForeignKey(null=True, blank=True, related_name='+', help_text='Optional. The image to use when sharing the page on social networks.', to='localore_admin.LocaloreImage', on_delete=django.db.models.deletion.SET_NULL)),
            ],
            options={
                'verbose_name': 'Live Feed',
            },
            bases=('wagtailcore.page', models.Model),
        ),
    ]
