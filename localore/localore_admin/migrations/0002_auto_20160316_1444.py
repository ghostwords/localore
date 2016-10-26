# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import wagtail.wagtailsearch.index
import wagtail.wagtailimages.models
import wagtail.wagtailcore.models
import taggit.managers
from django.conf import settings
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0028_merge'),
        ('wagtailimages', '0012_copy_image_permissions_to_collections'),
        ('taggit', '0002_auto_20150616_2121'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('localore_admin', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LocaloreImage',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='title')),
                ('file', models.ImageField(upload_to=wagtail.wagtailimages.models.get_upload_to, verbose_name='file', width_field='width', height_field='height')),
                ('width', models.IntegerField(verbose_name='width', editable=False)),
                ('height', models.IntegerField(verbose_name='height', editable=False)),
                ('created_at', models.DateTimeField(db_index=True, auto_now_add=True, verbose_name='created at')),
                ('focal_point_x', models.PositiveIntegerField(blank=True, null=True)),
                ('focal_point_y', models.PositiveIntegerField(blank=True, null=True)),
                ('focal_point_width', models.PositiveIntegerField(blank=True, null=True)),
                ('focal_point_height', models.PositiveIntegerField(blank=True, null=True)),
                ('file_size', models.PositiveIntegerField(null=True, editable=False)),
                ('alt', models.CharField(help_text="Describe the image's content and functionality for visually impaired users. Leave this blank in case of decorative images. See <a href='http://webaim.org/articles/gonewild/'>here</a> for more information.", blank=True, max_length=255)),
                ('collection', models.ForeignKey(default=wagtail.wagtailcore.models.get_root_collection_id, to='wagtailcore.Collection', related_name='+', verbose_name='collection')),
                ('tags', taggit.managers.TaggableManager(help_text=None, verbose_name='tags', to='taggit.Tag', blank=True, through='taggit.TaggedItem')),
                ('uploaded_by_user', models.ForeignKey(null=True, verbose_name='uploaded by user', on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, blank=True, editable=False)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model, wagtail.wagtailsearch.index.Indexed),
        ),
        migrations.CreateModel(
            name='LocaloreRendition',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('file', models.ImageField(upload_to='images', width_field='width', height_field='height')),
                ('width', models.IntegerField(editable=False)),
                ('height', models.IntegerField(editable=False)),
                ('focal_point_key', models.CharField(blank=True, max_length=255, editable=False, default='')),
                ('filter', models.ForeignKey(to='wagtailimages.Filter', related_name='+')),
                ('image', models.ForeignKey(to='localore_admin.LocaloreImage', related_name='renditions')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='localorerendition',
            unique_together=set([('image', 'filter', 'focal_point_key')]),
        ),
    ]
