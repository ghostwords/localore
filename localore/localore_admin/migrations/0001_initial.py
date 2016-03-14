# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0023_alter_page_revision_on_delete_behaviour'),
    ]

    operations = [
        migrations.CreateModel(
            name='JuicerSettings',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('juicer_auth_token', models.CharField(max_length=200, help_text='Your Juicer API authentication token.')),
                ('juicer_feed_id', models.CharField(max_length=200, help_text='Your Juicer feed ID.')),
                ('site', models.OneToOneField(to='wagtailcore.Site', editable=False)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
