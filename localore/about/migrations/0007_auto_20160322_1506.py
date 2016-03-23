# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0006_aboutcontactpage_aboutmissionpage_aboutmissionpagerelatedlink'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutmissionpage',
            name='description_bottom',
            field=wagtail.wagtailcore.fields.RichTextField(verbose_name='Bottom description'),
        ),
        migrations.AlterField(
            model_name='aboutmissionpage',
            name='description_top',
            field=wagtail.wagtailcore.fields.RichTextField(verbose_name='Top description'),
        ),
        migrations.AlterField(
            model_name='aboutmissionpagerelatedlink',
            name='link_page',
            field=models.ForeignKey(to='wagtailcore.Page', blank=True, verbose_name='Internal link', null=True, related_name='+'),
        ),
        migrations.AlterField(
            model_name='aboutmissionpagerelatedlink',
            name='title',
            field=models.CharField(max_length=255),
        ),
    ]
