import datetime

from django.db import models
from django.http import JsonResponse
from django.shortcuts import redirect

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
        max_length=1,
        choices=DISPATCH_TYPE_CHOICES,
        default=DISPATCH_TYPE_VIDEO,
    )

    embed_url = models.URLField(
        "Embed URL",
        help_text="YouTube or SoundCloud"
    )

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

    def serve(self, request):
        if 'json' in request.GET:
            resp = {}

            resp['title'] = self.title

            prev_page = (
                DispatchPage.objects.live()
                .sibling_of(self, False)
                .filter(path__lte=self.path)
                .order_by('-path')
                .filter(dispatch_type=self.dispatch_type)
                .first()
            )
            resp['prev_url'] = prev_page.url + '?json' if prev_page else None

            next_page = (
                DispatchPage.objects.live()
                .sibling_of(self, False)
                .filter(path__gte=self.path)
                .order_by('path')
                .filter(dispatch_type=self.dispatch_type)
                .first()
            )
            resp['next_url'] = next_page.url + '?json' if next_page else None

            resp['embed_url'] = self.embed_url

            try:
                resp['embed_html'] = embeds.get_embed(self.embed_url).html
            except EmbedException:
                resp['embed_html'] = ''

            return JsonResponse(resp)
        else:

            index_url = self.dispatches_index.url + '?dispatch=' + self.url
            return redirect(index_url, permanent=False)


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
            DispatchPage.objects.live().descendant_of(self).order_by('-date')
        )

    def get_dispatch_type(self, request):
        return request.GET.get('t', self.default_dispatch_type)

    def get_context(self, request):
        dispatches = self.dispatches

        dispatches = dispatches.filter(
            dispatch_type=self.get_dispatch_type(request)
        )

        context = super(DispatchesIndexPage, self).get_context(request)
        context['dispatches'] = dispatches

        return context
