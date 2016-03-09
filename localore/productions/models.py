from django.db import models

from localflavor.us.models import USStateField

from wagtail.wagtailadmin.edit_handlers import (
    FieldPanel,
    MultiFieldPanel
)
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailcore.models import Page
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from wagtail.wagtailsearch import index


class ProductionPage(Page):
    city = models.CharField(max_length=255)
    state = USStateField()

    hero_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text="The large header/feature/hero image for this production."
    )

    # TODO optional feature video
    # https://github.com/torchbox/wagtail/issues/907
    # https://github.com/torchbox/wagtail/pull/1553

    logo_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text="The production's logo (optional)."
    )

    description = RichTextField()

    twitter_url = models.URLField("Twitter URL", blank=True)
    instagram_url = models.URLField("Instagram URL", blank=True)
    youtube_url = models.URLField("YouTube URL", blank=True)
    tumblr_url = models.URLField("Tumblr URL", blank=True)
    soundcloud_url = models.URLField("SoundCloud URL", blank=True)
    vine_url = models.URLField("Vine URL", blank=True)

    # TODO producer & collaborator info (opens to bio)
    # @property

    # TODO "mentioned in":
    # auto-generated links to connections that link to this production
    # @property

    # TODO juicer slider

    highlights = RichTextField(
        blank=True,
        help_text="Optional WYSIWYG area to highlight the production's work."
    )

    search_fields = Page.search_fields + (
        index.SearchField('city'),
        index.SearchField('state'),
        index.SearchField('description', partial_match=True),
        index.SearchField('highlights', partial_match=True),
    )

    content_panels = Page.content_panels + [
        FieldPanel('city'),
        FieldPanel('state'),
        ImageChooserPanel('hero_image'),
        ImageChooserPanel('logo_image'),
        FieldPanel('description', classname='full'),
        MultiFieldPanel(
            [
                FieldPanel('twitter_url'),
                FieldPanel('instagram_url'),
                FieldPanel('youtube_url'),
                FieldPanel('tumblr_url'),
                FieldPanel('soundcloud_url'),
                FieldPanel('vine_url')
            ],
            heading="Social Links",
            classname="collapsible collapsed"
        ),
        FieldPanel('highlights', classname='full'),
    ]

    parent_page_types = ['productions.ProductionsIndexPage']
    subpage_types = []

    class Meta:
        verbose_name = "production"


class ProductionsIndexPage(Page):
    subpage_types = ['productions.ProductionPage']

    @property
    def productions(self):
        return (
            ProductionPage.objects.live().descendant_of(self)
            .order_by('-date')
        )
