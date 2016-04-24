import datetime
import json

from django.db import models
from django.http import JsonResponse

from localflavor.us.models import USStateField

from wagtail.wagtailadmin.edit_handlers import (
    FieldPanel,
    MultiFieldPanel,
)
from wagtail.wagtailcore.models import Page
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailembeds import embeds
from wagtail.wagtailembeds.exceptions import EmbedException
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from wagtail.wagtailsearch import index


DISPATCH_TYPE_VIDEO = 'v'
DISPATCH_TYPE_AUDIO = 'a'
DISPATCH_TYPE_CHOICES = (
    (DISPATCH_TYPE_VIDEO, 'Video'),
    (DISPATCH_TYPE_AUDIO, 'Audio'),
)


class DispatchPage(Page):
    date = models.DateField(default=datetime.date.today)
    is_featured = models.BooleanField(
        "featured",
        default=False,
        help_text=(
            "Makes this dispatch go to the top of the list in its category."
        ),
    )

    city = models.CharField(max_length=255)
    state = USStateField()

    description = RichTextField(blank=True)

    poster_image = models.ForeignKey(
        'localore_admin.LocaloreImage',
        null=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    dispatch_type = models.CharField(
        "category",
        max_length=1,
        choices=DISPATCH_TYPE_CHOICES,
        default=DISPATCH_TYPE_VIDEO,
    )

    embed_url = models.URLField(
        "Embed URL",
        help_text="YouTube or SoundCloud"
    )

    search_fields = Page.search_fields + (
        index.SearchField('city'),
        index.SearchField('state'),
        index.SearchField('get_state_display'),
        index.SearchField('description', partial_match=True),
    )

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('date'),
            FieldPanel('is_featured'),
        ], "Index page order"),
        MultiFieldPanel(
            [FieldPanel('city'), FieldPanel('state')],
            "Location"
        ),
        FieldPanel('description', classname="full"),
        ImageChooserPanel('poster_image'),
        FieldPanel('dispatch_type'),
        FieldPanel('embed_url'),
    ]

    parent_page_types = ['dispatches.DispatchesIndexPage']
    subpage_types = []

    @property
    def dispatches_index(self):
        return self.get_ancestors().type(DispatchesIndexPage).last()

    # TODO refactor (similar def in blog/models.py)
    # TODO cache?
    @property
    def prev_page(self):
        ordered_items = (
            DispatchPage.objects.live().sibling_of(self, inclusive=True)
            .filter(dispatch_type=self.dispatch_type)
            .order_by('-is_featured', '-date', '-pk')
        )
        prev_item = None
        for item in ordered_items:
            if item == self:
                return prev_item
            prev_item = item

    # TODO refactor (similar def in blog/models.py)
    # TODO cache?
    @property
    def next_page(self):
        ordered_items = (
            DispatchPage.objects.live().sibling_of(self, inclusive=True)
            .filter(dispatch_type=self.dispatch_type)
            .order_by('is_featured', 'date', 'pk')
        )
        prev_item = None
        for item in ordered_items:
            if item == self:
                return prev_item
            prev_item = item

    @property
    def data(self):
        data = {
            'title': self.title
        }

        prev_page = self.prev_page
        data['prev_url'] = prev_page.url if prev_page else None

        next_page = self.next_page
        data['next_url'] = next_page.url if next_page else None

        data['embed_url'] = self.embed_url

        try:
            data['embed_html'] = embeds.get_embed(self.embed_url).html
        except EmbedException:
            data['embed_html'] = ''

        return data

    def serve(self, request):
        if 'json' in request.GET:
            return JsonResponse(self.data)

        return super().serve(request)

    def get_context(self, request):
        index_page = self.dispatches_index.specific
        context = super().get_context(request)

        context['data'] = json.dumps(self.data)
        context['dispatches'] = (
            index_page.dispatches.filter(dispatch_type=self.dispatch_type)
        )
        context['dispatch_type'] = self.dispatch_type
        context['index_page'] = index_page

        return context

    class Meta:
        verbose_name = "Dispatch"


class DispatchesIndexPage(Page):
    subtitle = models.CharField(max_length=255, blank=True)
    intro = RichTextField(blank=True)

    default_dispatch_type = models.CharField(
        max_length=1,
        choices=DISPATCH_TYPE_CHOICES,
        default=DISPATCH_TYPE_VIDEO,
    )

    content_panels = Page.content_panels + [
        FieldPanel('subtitle', classname="full"),
        FieldPanel('intro', classname="full"),
        FieldPanel('default_dispatch_type'),
    ]

    subpage_types = ['dispatches.DispatchPage']

    @property
    def dispatches(self):
        return (
            DispatchPage.objects.live().descendant_of(self)
            .select_related('poster_image')
            .order_by('-is_featured', '-date', '-pk')
        )

    def get_context(self, request):
        context = super().get_context(request)
        context['dispatches'] = self.dispatches.filter(
            dispatch_type=request.GET.get('t', self.default_dispatch_type)
        )
        context['dispatch_type'] = self.default_dispatch_type
        context['index_page'] = self
        return context

    class Meta:
        verbose_name = "Dispatches Index"
