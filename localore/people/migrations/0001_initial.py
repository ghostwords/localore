# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0010_change_on_delete_behaviour'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('role', models.CharField(max_length=255, blank=True)),
                ('biography', wagtail.wagtailcore.fields.RichTextField()),
                ('email', models.EmailField(max_length=254, blank=True)),
                ('twitter_url', models.URLField(blank=True, verbose_name='Twitter URL')),
                ('instagram_url', models.URLField(blank=True, verbose_name='Instagram URL')),
                ('photo', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='wagtailimages.Image', related_name='+')),
            ],
            options={
                'verbose_name_plural': 'people',
                'verbose_name': 'person',
            },
        ),
    ]
