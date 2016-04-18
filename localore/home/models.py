from django.db import models
from django.utils.html import format_html

from wagtail.wagtailadmin.edit_handlers import (
    FieldPanel,
    PageChooserPanel,
    MultiFieldPanel,
)
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailcore.models import Page
from wagtail.wagtaildocs.edit_handlers import DocumentChooserPanel
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel


class HomePage(Page):
    site_intro = RichTextField(blank=True)

    related_content_title = models.CharField(
        verbose_name="title",
        max_length=255,
    )
    related_content_page = models.ForeignKey(
        'wagtailcore.Page',
        verbose_name="page to link to",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    related_content_subtitle = models.CharField(
        verbose_name="subtitle",
        max_length=255,
        blank=True,
        default="Across America"
    )

    video_poster_image = models.ForeignKey(
        'localore_admin.LocaloreImage',
        verbose_name="poster image",
        null=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    video_mp4 = models.ForeignKey(
        'wagtaildocs.Document',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    video_webm = models.ForeignKey(
        'wagtaildocs.Document',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    video_ogv = models.ForeignKey(
        'wagtaildocs.Document',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    video_youtube_id = models.CharField(
        verbose_name="YouTube video ID",
        max_length=12,
        default="j6IIjLK-8fU",
        help_text=format_html(
            "The part in bold: "
            "https://www.youtube.com/watch?v=<b>j6IIjLK-8fU</b>"
        ),
    )
    video_is_360 = models.BooleanField(
        "360˚ video",
        default=False,
        help_text="This is a 360-degree video.",
    )

    view_more_title = models.CharField(
        verbose_name='"View more" link title',
        max_length=255,
        help_text='For example, "View more connections"',
    )
    view_more_page = models.ForeignKey(
        'wagtailcore.Page',
        verbose_name="Page to link to",
        null=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    live_feed_intro = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('site_intro', classname="full"),
        MultiFieldPanel([
            FieldPanel('related_content_title'),
            FieldPanel('related_content_subtitle'),
            PageChooserPanel('related_content_page'),
        ], "Featured content"),
        MultiFieldPanel([
            ImageChooserPanel('video_poster_image'),
            DocumentChooserPanel('video_mp4'),
            DocumentChooserPanel('video_webm'),
            DocumentChooserPanel('video_ogv'),
        ], "Hero section"),
        MultiFieldPanel([
            FieldPanel('video_youtube_id'),
            FieldPanel('video_is_360'),
            FieldPanel('view_more_title'),
            PageChooserPanel('view_more_page'),
        ], "Fullscreen video"),
        FieldPanel('live_feed_intro', classname="full"),
    ]

    parent_page_types = []

    class Meta:
        verbose_name = "Homepage"
