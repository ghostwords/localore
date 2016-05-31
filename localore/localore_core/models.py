from django.db import models

from wagtail.wagtailadmin.edit_handlers import (
    FieldPanel,
    MultiFieldPanel,
)
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel


class LocalorePromoteFields(models.Model):
    social_image = models.ForeignKey(
        'localore_admin.LocaloreImage',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text=(
            "Optional. "
            "The image to use when sharing the page on social networks."
        )
    )

    promote_panels = [
        MultiFieldPanel([
            FieldPanel('seo_title'),
            FieldPanel('slug'),
        ], "Common page configuration"),

        MultiFieldPanel([
            ImageChooserPanel('social_image'),
            FieldPanel('search_description'),
        ], "Social networks"),

        MultiFieldPanel([
            FieldPanel('show_in_menus'),
        ], "Cross-page behavior"),
    ]

    class Meta:
        abstract = True
