from django.db import models
from django.utils.html import format_html

from modelcluster.fields import ParentalKey

from wagtail.wagtailadmin.edit_handlers import (
    FieldPanel,
    InlinePanel,
    MultiFieldPanel,
    PageChooserPanel,
)
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailcore.models import Page, Orderable
from wagtail.wagtaildocs.edit_handlers import DocumentChooserPanel
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel

from localore_core.models import LocalorePromoteFields


class FeaturedPage(models.Model):
    featured_page = models.ForeignKey(
        'wagtailcore.Page',
        verbose_name="page to feature",
        on_delete=models.CASCADE,
        related_name='+'
    )

    title = models.CharField(
        max_length=255,
        blank=True,
        help_text="Leave blank to use page title.")

    subtitle = models.CharField(max_length=255)

    panels = [
        PageChooserPanel('featured_page'),
        FieldPanel('title'),
        FieldPanel('subtitle'),
    ]

    class Meta:
        abstract = True


class HomePageFeaturedPage(Orderable, FeaturedPage):
    home_page = ParentalKey('HomePage', related_name='featured_pages')


class HomePage(Page, LocalorePromoteFields):
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
    video_poster_image_mobile = models.ForeignKey(
        'localore_admin.LocaloreImage',
        verbose_name="poster image (mobile)",
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

    content_panels = Page.content_panels + [
        FieldPanel('site_intro', classname="full"),
        MultiFieldPanel([
            FieldPanel('related_content_title'),
            FieldPanel('related_content_subtitle'),
            PageChooserPanel('related_content_page'),
        ], "Featured content"),
        MultiFieldPanel([
            ImageChooserPanel('video_poster_image'),
            ImageChooserPanel('video_poster_image_mobile'),
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
        InlinePanel(
            'featured_pages',
            label="Featured Pages",
            min_num=3,
            max_num=3,
        ),
    ]

    promote_panels = LocalorePromoteFields.promote_panels

    parent_page_types = []

    @property
    def video_poster_image_file_extension(self):
        return self.video_poster_image.file.url.split('.')[-1]

    @property
    def preview_modes(self):
        return super(HomePage, self).preview_modes + [
            ('no-video', 'Preview poster image'),
        ]

    def serve_preview(self, request, mode_name):
        if mode_name == 'no-video':
            self.video_mp4 = None

        return super(HomePage, self).serve_preview(request, mode_name)

    class Meta:
        verbose_name = "Homepage"


class LiveFeedPage(Page, LocalorePromoteFields):
    live_feed_intro = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('live_feed_intro', classname="full"),
    ]

    promote_panels = LocalorePromoteFields.promote_panels

    child_page_types = []

    class Meta:
        verbose_name = "Live Feed"
