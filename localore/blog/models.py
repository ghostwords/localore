from django.db import models

from modelcluster.fields import ParentalKey

from wagtail.wagtailcore.models import Page, Orderable
from wagtail.wagtailcore.fields import RichTextField, StreamField
from wagtail.wagtailcore.blocks import (
    CharBlock,
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
from wagtail.wagtailembeds.blocks import EmbedBlock
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from wagtail.wagtailimages.blocks import ImageChooserBlock
from wagtail.wagtailsearch import index

import datetime


class QuoteBlock(StructBlock):
    quote = TextBlock("quote title")
    attribution = CharBlock()

    class Meta:
        template = 'blog/blocks/quote.html'
        icon = 'openquote'
        #label = 'Quote'


class BlogPage(Page):
    main_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    date = models.DateField("Post date", default=datetime.date.today)

    body = StreamField([
        ('heading', CharBlock(
            classname="full title",
            icon='title',
            template='blog/blocks/heading.html'
        )),
        ('quote', QuoteBlock()),
        ('paragraph',
            RichTextBlock(icon='doc-full', label='Rich Text')),
        ('image', ImageChooserBlock(icon='image')),
        ('embed', EmbedBlock(icon='media')),
    ])

    # search index config
    search_fields = Page.search_fields + (
        index.SearchField('body'),
    )

    # admin editor panels config
    content_panels = Page.content_panels + [
        FieldPanel('date'),
        ImageChooserPanel('main_image'),
        StreamFieldPanel('body')
    ]

    # parent page/subpage type rules
    parent_page_types = ['blog.BlogIndexPage']
    subpage_types = []

    @property
    def blog_index(self):
        return self.get_ancestors().type(BlogIndexPage).last()


class LinkFields(models.Model):
    link_external = models.URLField(
        "External link",
        blank=True,
        max_length=500
    )
    link_page = models.ForeignKey(
        'blog.BlogPage',
        null=True,
        blank=True,
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
    title = models.CharField(max_length=255, help_text="Link title")

    panels = [
        FieldPanel('title'),
        MultiFieldPanel(LinkFields.panels, "Link"),
    ]

    class Meta:
        abstract = True


class BlogIndexRelatedLink(Orderable, RelatedLink):
    page = ParentalKey('BlogIndexPage', related_name='related_links')


class BlogIndexPage(Page):
    body = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('body', classname="full"),
        InlinePanel('related_links', label="Featured posts"),
    ]

    subpage_types = ['blog.BlogPage']
