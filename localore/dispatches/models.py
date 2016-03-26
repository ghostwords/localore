import datetime

from django.db import models

from localflavor.us.models import USStateField

from wagtail.wagtailcore.models import Page
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailadmin.edit_handlers import (
    FieldPanel,
    MultiFieldPanel,
)
from wagtail.wagtailsearch import index

from wagtail_embed_videos.edit_handlers import EmbedVideoChooserPanel


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
    video = models.ForeignKey(
        'wagtail_embed_videos.EmbedVideo',
        verbose_name="Video",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    content_panels = DispatchPage.content_panels + [
        EmbedVideoChooserPanel('video'),
    ]

    parent_page_types = ['dispatches.VideoDispatchesIndexPage']
    subpage_types = []

    @property
    def get_video_url(self):
        return self.video.url

    @property
    def get_video_thumbnail(self):
        return self.video.thumbnail

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

    class Meta:
        abstract = True


class VideoDispatchesIndexPage(DispatchesIndexPage):
    # pylint: disable=too-many-ancestors
    subpage_types = ['dispatches.VideoDispatchPage']

    @property
    def dispatches(self):
        return (
            VideoDispatchPage.objects.live().descendant_of(self)
            .order_by('-date')
        )


class AudioDispatchesIndexPage(DispatchesIndexPage):
    # pylint: disable=too-many-ancestors
    subpage_types = ['dispatches.AudioDispatchPage']

    @property
    def dispatches(self):
        return (
            AudioDispatchPage.objects.live().descendant_of(self)
            .order_by('-date')
        )
