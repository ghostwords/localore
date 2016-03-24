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
    description_top = RichTextField("Top description")
    description_bottom = RichTextField("Bottom description")

    search_fields = Page.search_fields + (
        index.SearchField('description_top', partial_match=True),
        index.SearchField('description_bottom', partial_match=True),
    )

    content_panels = Page.content_panels + [
        FieldPanel('description_top', classname='full'),
        FieldPanel('description_bottom', classname='full'),
        InlinePanel('related_links', label="Related links"),
    ]

    parent_page_types = ['home.HomePage', 'localore_admin.PageAlias']
    subpage_types = []


class AboutTeamPageRelatedPerson(Orderable, PersonField):
    page = ParentalKey('AboutTeamPage', related_name='related_people')


class AboutTeamPage(Page):
    description = RichTextField()

    search_fields = Page.search_fields + (
        index.SearchField('description', partial_match=True),
    )

    content_panels = Page.content_panels + [
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


class AboutContactPage(Page):
    contact_information = RichTextField()

    search_fields = Page.search_fields + (
        index.SearchField('contact_information', partial_match=True),
    )

    content_panels = Page.content_panels + [
        FieldPanel('contact_information', classname='full'),
    ]

    parent_page_types = ['home.HomePage', 'localore_admin.PageAlias']
    subpage_types = []
