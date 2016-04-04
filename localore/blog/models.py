import datetime

from django.db import models
from django.utils.html import format_html

from modelcluster.fields import ParentalKey

from wagtail.wagtailcore.models import Page, Orderable
from wagtail.wagtailcore.fields import RichTextField, StreamField
from wagtail.wagtailcore.blocks import (
    CharBlock,
    RawHTMLBlock,
    RichTextBlock,
    StructBlock,
    TextBlock
)
from wagtail.wagtailadmin.edit_handlers import (
    FieldPanel,
    InlinePanel,
    MultiFieldPanel,
    PageChooserPanel,
    StreamFieldPanel,
)
from wagtail.wagtaildocs.edit_handlers import DocumentChooserPanel
from wagtail.wagtailembeds.blocks import EmbedBlock
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from wagtail.wagtailimages.blocks import ImageChooserBlock
from wagtail.wagtailsearch import index


class AssociatedProduction(models.Model):
    production_page = models.ForeignKey(
        'productions.ProductionPage',
        on_delete=models.CASCADE,
        related_name='+'
    )

    panels = [
        PageChooserPanel('production_page'),
    ]

    class Meta:
        abstract = True


class BlogPageAssociatedProduction(Orderable, AssociatedProduction):
    page = ParentalKey('BlogPage', related_name='associated_productions')


class RelatedConnection(models.Model):
    related_blog_page = models.ForeignKey(
        'blog.BlogPage',
        verbose_name="Related Connection",
        on_delete=models.CASCADE,
        related_name='+'
    )

    panels = [
        PageChooserPanel('related_blog_page'),
    ]

    class Meta:
        abstract = True


class BlogPageRelatedConnection(Orderable, RelatedConnection):
    page = ParentalKey('BlogPage', related_name='related_posts')


class QuoteBlock(StructBlock):
    quote = TextBlock("quote title")
    attribution = CharBlock()

    class Meta:
        template = 'blog/blocks/quote.html'
        icon = 'openquote'
        #label = 'Quote'


class BlogPage(Page):
    subtitle = models.CharField(max_length=255, blank=True)

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
        blank=True,
        help_text=format_html(
            "The part in bold: "
            "https://www.youtube.com/watch?v=<b>j6IIjLK-8fU</b>"
        ),
    )

    date = models.DateField("Post date", default=datetime.date.today)

    intro = RichTextField(blank=True)

    body = StreamField([
        ('heading', CharBlock(
            classname="full title",
            icon='title',
            template='blog/blocks/heading.html'
        )),
        ('quote', QuoteBlock()),
        ('paragraph', RichTextBlock(icon='doc-full', label="Rich Text")),
        ('image', ImageChooserBlock(icon='image')),
        ('embed', EmbedBlock(icon='media')),
        ('raw_html', RawHTMLBlock(
            icon='code',
            label="Raw HTML",
            help_text=format_html(
                '<ul class="messages"><li class="error">Please mind that '
                'using raw HTML can break site rendering and/or compromise '
                'site security.</li></ul>'
            ),
        )),
    ])

    # search index config
    search_fields = Page.search_fields + (
        index.SearchField('body', partial_match=True),
    )

    # admin editor panels config
    content_panels = Page.content_panels + [
        FieldPanel('subtitle', classname='full'),
        FieldPanel('date'),
        MultiFieldPanel([
            ImageChooserPanel('video_poster_image'),
            DocumentChooserPanel('video_mp4'),
            DocumentChooserPanel('video_webm'),
            DocumentChooserPanel('video_ogv'),
        ], "Hero section"),
        MultiFieldPanel([
            FieldPanel('video_youtube_id'),
        ], "Fullscreen video"),
        FieldPanel('intro', classname='full'),
        StreamFieldPanel('body'),
        InlinePanel('associated_productions', label="Associated Productions"),
        InlinePanel('related_posts', label="Related Connections"),
    ]

    # parent page/subpage type rules
    parent_page_types = ['blog.BlogIndexPage']
    subpage_types = []

    @property
    def blog_index(self):
        return self.get_ancestors().type(BlogIndexPage).last()

    class Meta:
        verbose_name = "connection"


class LinkFields(models.Model):
    link_external = models.CharField(
        "External link",
        max_length=500,
        blank=True,
        help_text="Please provide an external URL, or select a page below."
    )
    link_page = models.ForeignKey(
        Page,
        verbose_name="Internal link",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    @property
    def link(self):
        if self.link_page:
            return self.link_page.url
        else:
            return self.link_external

    panels = [
        FieldPanel('link_external'),
        PageChooserPanel('link_page'),
    ]

    class Meta:
        abstract = True


class RelatedLink(LinkFields):
    title = models.CharField(max_length=255)

    panels = [
        FieldPanel('title'),
        MultiFieldPanel(LinkFields.panels, "Link"),
    ]

    class Meta:
        abstract = True


class BlogIndexRelatedLink(Orderable, RelatedLink):
    page = ParentalKey('BlogIndexPage', related_name='related_links')


class BlogIndexPage(Page):
    subtitle = models.CharField(max_length=255, blank=True)

    intro = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('subtitle', classname="full"),
        FieldPanel('intro', classname="full"),
        InlinePanel('related_links', label="Featured posts"),
    ]

    subpage_types = ['blog.BlogPage']

    @property
    def posts(self):
        return BlogPage.objects.live().descendant_of(self).order_by('-date')

    class Meta:
        verbose_name = "connections index page"
