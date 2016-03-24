from django.core.exceptions import ValidationError
from django.db import models
from django.db.models.signals import pre_delete
from django.dispatch import receiver
from django.shortcuts import redirect
from django.utils.safestring import mark_safe

from wagtail.contrib.settings.models import BaseSetting, register_setting
from wagtail.wagtailadmin.edit_handlers import FieldPanel, MultiFieldPanel
from wagtail.wagtailcore.models import Page
from wagtail.wagtailimages.models import (
    Image,
    AbstractImage,
    AbstractRendition
)

from blog.models import LinkFields


# redirect page class

class PageAlias(Page, LinkFields): # pylint: disable=too-many-ancestors
    content_panels = Page.content_panels + [
        MultiFieldPanel(LinkFields.panels, "Redirect to"),
    ]

    parent_page_types = ['home.HomePage']

    def clean(self):
        if not self.link:
            raise ValidationError(
                "You must specify an alias pointing to an existing page "
                "or external URL."
            )

    def serve(self, request):
        return redirect(self.link, permanent=False)


# site settings

@register_setting(icon='site')
class JuicerSettings(BaseSetting):
    juicer_feed_id = models.CharField(
        max_length=200,
        help_text="Your Juicer feed ID."
    )
    juicer_auth_token = models.CharField(
        max_length=200,
        help_text="Your Juicer API authentication token."
    )

    panels = [
        FieldPanel('juicer_feed_id'),
        FieldPanel('juicer_auth_token'),
    ]


# custom image model

class LocaloreImage(AbstractImage):
    alt_text = models.CharField(
        max_length=255,
        blank=True,
        help_text=(mark_safe(
            "Describe the image's content and functionality for visually "
            "impaired users. Leave this blank in case of decorative images. "
            "See <a href='http://webaim.org/articles/gonewild/'>here</a> for "
            "more information."
        ))
    )

    admin_form_fields = Image.admin_form_fields + (
        'alt_text',
    )


class LocaloreRendition(AbstractRendition):
    image = models.ForeignKey('LocaloreImage', related_name='renditions')

    @property
    def alt(self):
        return self.image.alt_text

    class Meta:
        unique_together = (
            ('image', 'filter', 'focal_point_key'),
        )


@receiver(pre_delete, sender=LocaloreImage)
# pylint: disable=unused-argument
def image_delete(sender, instance, **kwargs):
    instance.file.delete(False)


@receiver(pre_delete, sender=LocaloreRendition)
# pylint: disable=unused-argument
def rendition_delete(sender, instance, **kwargs):
    instance.file.delete(False)
