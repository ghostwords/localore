import datetime

from django.db import models

from localflavor.us.models import USStateField

from wagtail.wagtailcore.models import Page
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailadmin.edit_handlers import (
    FieldPanel,
    MultiFieldPanel,
)
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from wagtail.wagtailsearch import index


class DispatchPage(Page):
    date = models.DateField("Post date", default=datetime.date.today)
    city = models.CharField(max_length=255)
    state = USStateField()
    description = RichTextField(blank=True)

    search_fields = Page.search_fields + (
        index.SearchField('location'),
        index.SearchField('description', partial_match=True),
    )

    content_panels = Page.content_panels + [
        FieldPanel('date'),
        MultiFieldPanel(
            [FieldPanel('city'), FieldPanel('state')],
            "Location"
        ),
        FieldPanel('description'),
    ]

    @property
    def dispatches_index(self):
        return self.get_ancestors().type(DispatchesIndexPage).last()

    class Meta:
        abstract = True


class VideoDispatchPage(DispatchPage):
    # pylint: disable=too-many-ancestors
    thumbnail = models.ForeignKey(
        'localore_admin.LocaloreImage',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    content_panels = DispatchPage.content_panels + [
        ImageChooserPanel('thumbnail'),
    ]

    parent_page_types = ['dispatches.VideoDispatchesIndexPage']
    subpage_types = []

    class Meta:
        verbose_name = "video dispatch"
        verbose_name_plural = "video dispatches"


class AudioDispatchPage(DispatchPage):
    # pylint: disable=too-many-ancestors
    parent_page_types = ['dispatches.AudioDispatchesIndexPage']
    subpage_types = []

    class Meta:
        verbose_name = "audio dispatch"
        verbose_name_plural = "audio dispatches"


class DispatchesIndexPage(Page):
    subtitle = models.CharField(max_length=255, blank=True)
    intro = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('subtitle', classname="full"),
        FieldPanel('intro', classname="full"),
    ]

    @property
    def dispatches(self):
        return (
            DispatchPage.objects.live().descendant_of(self)
            .order_by('-date')
        )

    class Meta:
        abstract = True


class VideoDispatchesIndexPage(DispatchesIndexPage):
    # pylint: disable=too-many-ancestors
    subpage_types = ['dispatches.VideoDispatchPage']


class AudioDispatchesIndexPage(DispatchesIndexPage):
    # pylint: disable=too-many-ancestors
    subpage_types = ['dispatches.AudioDispatchPage']
