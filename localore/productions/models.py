from django.db import models
from django.forms.widgets import RadioSelect

from localflavor.us.models import USStateField

from modelcluster.fields import ParentalKey

from wagtail.wagtailadmin.edit_handlers import (
    FieldPanel,
    InlinePanel,
    MultiFieldPanel
)
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailcore.models import Orderable, Page
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from wagtail.wagtailsearch import index
from wagtail.wagtailsnippets.edit_handlers import SnippetChooserPanel

from blog.models import BlogPageAssociatedProduction


class LinkField(models.Model):
    SERVICE_NAME_CHOICES = (
        ('', 'Other'),
        ('facebook', 'Facebook'),
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


class PersonField(models.Model):
    person = models.ForeignKey(
        'people.Person',
        on_delete=models.CASCADE,
        related_name='+',
        verbose_name="Name"
    )

    panels = [
        SnippetChooserPanel('person'),
    ]

    class Meta:
        abstract = True


class ProductionPageRelatedPerson(Orderable, PersonField):
    page = ParentalKey('ProductionPage', related_name='related_people')


class ProductionPageFeaturedPerson(Orderable, PersonField):
    page = ParentalKey('ProductionPage', related_name='featured_people')


class JuicerSourceField(models.Model):
    name = models.CharField(
        "source account or hashtag",
        max_length=100,
        help_text=(
            "Juicer source name, without # or @. Filters by account/hashtag "
            "within the feed across all services (Twitter, Facebook, ...)."
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
        'localore_admin.LocaloreImage',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text="The header/hero/feature image for this production."
    )

    tile_image = models.ForeignKey(
        'localore_admin.LocaloreImage',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text=(
            "Optional: "
            "The image to use on the grid view of the productions index page. "
            "Will use hero image if not set."
        )
    )

    logo_image = models.ForeignKey(
        'localore_admin.LocaloreImage',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text="The production's logo (optional)."
    )

    description = RichTextField()

    highlights = RichTextField(
        blank=True,
        help_text="Optional WYSIWYG area to highlight the production's work."
    )

    search_fields = Page.search_fields + (
        index.SearchField('city'),
        index.SearchField('state'),
        index.SearchField('get_state_display'),
        index.SearchField('description', partial_match=True),
        index.SearchField('highlights', partial_match=True),
    )

    content_panels = Page.content_panels + [
        MultiFieldPanel(
            [FieldPanel('city'), FieldPanel('state')],
            "Location"
        ),
        MultiFieldPanel([
            ImageChooserPanel('hero_image'),
            ImageChooserPanel('tile_image'),
            ImageChooserPanel('logo_image'),
        ], "Graphics"),
        FieldPanel('description', classname='full'),
        InlinePanel('related_links', label="Related links"),
        InlinePanel(
            'related_people',
            label="about page team members",
            help_text=(
                "Select the production's team members, and the order "
                "to display them in on the About: Team page."
            )
        ),
        InlinePanel(
            'featured_people',
            label="featured team members",
            max_num=4,
            help_text="Select up to four people to feature on this page."
        ),
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

    @property
    def mentioned_in(self):
        associations = BlogPageAssociatedProduction.objects.filter(
            production_page=self
        )
        return [item.page for item in associations]

    class Meta:
        verbose_name = "Production"


class ProductionsIndexPage(Page):
    DISPLAY_TYPE_GRID = 'g'
    DISPLAY_TYPE_LIST = 'l'
    DISPLAY_TYPE_CHOICES = (
        (DISPLAY_TYPE_GRID, 'Grid'),
        (DISPLAY_TYPE_LIST, 'List'),
    )

    subtitle = models.CharField(max_length=255, blank=True)

    intro = RichTextField(blank=True)

    default_view = models.CharField(
        max_length=1,
        choices=DISPLAY_TYPE_CHOICES,
        default=DISPLAY_TYPE_GRID
    )

    content_panels = Page.content_panels + [
        FieldPanel('subtitle', classname='full'),
        FieldPanel('intro', classname='full'),
        FieldPanel('default_view', widget=RadioSelect),
    ]

    subpage_types = ['productions.ProductionPage']

    @property
    def productions(self):
        return (
            ProductionPage.objects.live().descendant_of(self)
            .select_related('hero_image', 'tile_image')
        )

    def get_context(self, request):
        context = super(ProductionsIndexPage, self).get_context(request)

        context['DISPLAY_TYPE_GRID'] = ProductionsIndexPage.DISPLAY_TYPE_GRID
        context['DISPLAY_TYPE_LIST'] = ProductionsIndexPage.DISPLAY_TYPE_LIST
        context['use_list_view'] = (
            request.GET.get('t', self.default_view) ==
            ProductionsIndexPage.DISPLAY_TYPE_LIST
        )

        return context

    class Meta:
        verbose_name = "Productions Index"
