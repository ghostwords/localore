from django.db import models

from modelcluster.fields import ParentalKey

from wagtail.wagtailadmin.edit_handlers import FieldPanel, InlinePanel
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailcore.models import Orderable, Page
from wagtail.wagtailsearch import index

from blog.models import RelatedLink
from productions.models import PersonField


class AboutMissionPageRelatedLink(Orderable, RelatedLink):
    page = ParentalKey('AboutMissionPage', related_name='related_links')


class AboutMissionPage(Page):
    subtitle = models.CharField(max_length=255, blank=True)
    description = RichTextField()
    org_description = RichTextField(verbose_name="Organizational Description")

    search_fields = Page.search_fields + (
        index.SearchField('subtitle', partial_match=True),
        index.SearchField('description', partial_match=True),
        index.SearchField('org_description', partial_match=True),
    )

    content_panels = Page.content_panels + [
        FieldPanel('subtitle', classname='full'),
        FieldPanel('description', classname='full'),
        FieldPanel('org_description', classname='full'),
        InlinePanel('related_links', label="Related links"),
    ]

    parent_page_types = ['home.HomePage', 'localore_admin.PageAlias']
    subpage_types = []

    class Meta:
        verbose_name = "About: Mission"


class AboutTeamPageRelatedPerson(Orderable, PersonField):
    page = ParentalKey('AboutTeamPage', related_name='related_people')


class AboutTeamPage(Page):
    subtitle = models.CharField(max_length=255, blank=True)
    description = RichTextField()

    search_fields = Page.search_fields + (
        index.SearchField('subtitle', partial_match=True),
        index.SearchField('description', partial_match=True),
    )

    content_panels = Page.content_panels + [
        FieldPanel('subtitle', classname='full'),
        FieldPanel('description', classname='full'),
        InlinePanel(
            'related_people',
            label="AIR | Localore staff",
            help_text=(
                "Select the AIR | Localore staff, and the order "
                "to display them in on this page."
            )
        ),
    ]

    parent_page_types = ['home.HomePage', 'localore_admin.PageAlias']
    subpage_types = []

    @property
    def localore_staff(self):
        return self.related_people.select_related('person__photo').all()

    class Meta:
        verbose_name = "About: Team"


class AboutContactPage(Page):
    subtitle = models.CharField(max_length=255, blank=True)
    contact_information = RichTextField()

    search_fields = Page.search_fields + (
        index.SearchField('subtitle', partial_match=True),
        index.SearchField('contact_information', partial_match=True),
    )

    content_panels = Page.content_panels + [
        FieldPanel('subtitle', classname='full'),
        FieldPanel('contact_information', classname='full'),
    ]

    parent_page_types = ['home.HomePage', 'localore_admin.PageAlias']
    subpage_types = []

    class Meta:
        verbose_name = "About: Connect"
