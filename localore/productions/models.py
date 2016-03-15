from django.db import models

from localflavor.us.models import USStateField

from modelcluster.fields import ParentalKey

from wagtail.wagtailadmin.edit_handlers import (
    FieldPanel,
    InlinePanel,
    MultiFieldPanel
)
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailcore.models import Page
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from wagtail.wagtailsearch import index


class LinkField(models.Model):
    SERVICE_NAME_CHOICES = (
        ('', 'Other'),
        ('instagram', 'Instagram'),
        ('soundcloud', 'SoundCloud'),
        ('tumblr', 'Tumblr'),
        ('twitter', 'Twitter'),
        ('vimeo', 'Vimeo'),
        ('youtube', 'YouTube'),
    )

    service_name = models.CharField(
        "service",
        max_length=10,
        choices=SERVICE_NAME_CHOICES,
        blank=True
    )
    url = models.URLField("URL")

    panels = [
        FieldPanel('service_name'),
        FieldPanel('url'),
    ]

    class Meta:
        abstract = True


class ProductionPageRelatedLink(LinkField):
    page = ParentalKey('ProductionPage', related_name='related_links')


class JuicerSourceField(models.Model):
    name = models.CharField(
        "source account name",
        max_length=100,
        help_text=(
            "Juicer source account name, without # or @. "
            "Filters across all account types in the feed."
        )
    )

    panels = [
        FieldPanel('name'),
    ]

    class Meta:
        abstract = True


class ProductionPageJuicerSource(JuicerSourceField):
    page = ParentalKey('ProductionPage', related_name='juicer_sources')


class ProductionPage(Page):
    city = models.CharField(max_length=255)
    state = USStateField()

    hero_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text="The header/hero/feature image for this production."
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

    # TODO producer & collaborator info (opens to bio)
    # @property

    # TODO "mentioned in":
    # auto-generated links to connections that link to this production
    # @property

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
        MultiFieldPanel(
            [FieldPanel('city'), FieldPanel('state')],
            "Location"
        ),
        MultiFieldPanel(
            [ImageChooserPanel('hero_image'), ImageChooserPanel('logo_image')],
            "Graphics"
        ),
        FieldPanel('description', classname='full'),
        InlinePanel('related_links', label="Related links"),
        FieldPanel('highlights', classname='full'),
        InlinePanel('juicer_sources', label="Juicer sources"),
    ]

    parent_page_types = ['productions.ProductionsIndexPage']
    subpage_types = []

    @property
    def juicer_feed_filter(self):
        return ",".join(
            source.name for source in self.juicer_sources.all()
        )

    @property
    def productions_index(self):
        return self.get_ancestors().type(ProductionsIndexPage).last()

    class Meta:
        verbose_name = "production"


class ProductionsIndexPage(Page):
    subpage_types = ['productions.ProductionPage']

    @property
    def productions(self):
        return ProductionPage.objects.live().descendant_of(self)
