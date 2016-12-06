import datetime

from django.db import models

from wagtail.wagtailadmin.edit_handlers import (
    FieldPanel,
    MultiFieldPanel,
    StreamFieldPanel,
)
from wagtail.wagtailcore.fields import RichTextField, StreamField
from wagtail.wagtailcore.models import Page
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from wagtail.wagtailsearch import index

from blog.models import BlogBodyBlock
from localore_core.models import LocalorePromoteFields


class PresidentPage(Page, LocalorePromoteFields):
    subtitle = models.CharField(max_length=255, blank=True)

    hero_image = models.ForeignKey(
        'localore_admin.LocaloreImage',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text=(
            "Optional: "
            "The header/hero/feature image for this President Series post."
        )
    )

    tile_image = models.ForeignKey(
        'localore_admin.LocaloreImage',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text=(
            "The image to use on the President Series index page."
        )
    )

    image_credit_caption = RichTextField(
        verbose_name="credit caption",
        blank=True,
        help_text="Optional: Goes under the hero image."
    )

    intro = StreamField(BlogBodyBlock)

    aired_on_date = models.DateField(default=datetime.date.today)

    body = StreamField(
        BlogBodyBlock,
        blank=True,
    )

    search_fields = Page.search_fields + [
        index.SearchField('subtitle', partial_match=True),
        index.SearchField('intro', partial_match=True),
        index.SearchField('body', partial_match=True),
    ]

    content_panels = Page.content_panels + [
        FieldPanel('subtitle', classname='full'),
        FieldPanel('aired_on_date'),
        MultiFieldPanel([
            ImageChooserPanel('tile_image'),
            ImageChooserPanel('hero_image'),
            FieldPanel('image_credit_caption'),
        ], "Graphics"),
        StreamFieldPanel('intro'),
        StreamFieldPanel('body'),
    ]

    promote_panels = LocalorePromoteFields.promote_panels

    parent_page_types = ['president.PresidentIndexPage']
    subpage_types = []

    class Meta:
        verbose_name = "President Series Post"


class PresidentIndexPage(Page, LocalorePromoteFields):
    subtitle = models.CharField(max_length=255, blank=True)

    intro = RichTextField(blank=True)

    share_your_story_text = RichTextField(
        verbose_name="Share Your Story text"
    )

    content_panels = Page.content_panels + [
        FieldPanel('subtitle', classname='full'),
        FieldPanel('intro', classname='full'),
        FieldPanel('share_your_story_text', classname='full'),
    ]

    promote_panels = LocalorePromoteFields.promote_panels

    subpage_types = ['president.PresidentPage']

    @property
    def posts(self):
        if self.live:
            children = PresidentPage.objects.live().descendant_of(self)
        else:
            children = PresidentPage.objects.descendant_of(self)
        return children.select_related('hero_image', 'tile_image')

    class Meta:
        verbose_name = "President Series Index"
