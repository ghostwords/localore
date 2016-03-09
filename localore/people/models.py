from django.db import models

from wagtail.wagtailadmin.edit_handlers import (
    FieldPanel,
    MultiFieldPanel,
    PageChooserPanel
)
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from wagtail.wagtailsearch import index
from wagtail.wagtailsnippets.models import register_snippet


@register_snippet
class Person(models.Model, index.Indexed):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    role = models.CharField(max_length=255, blank=True)

    photo = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    production = models.ForeignKey(
        'productions.ProductionPage',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name="associated production",
        help_text="Leave blank for AIR/Localore staff."
    )

    biography = RichTextField()

    email = models.EmailField(blank=True)
    twitter_url = models.URLField("Twitter URL", blank=True)
    instagram_url = models.URLField("Instagram URL", blank=True)

    search_fields = (
        index.SearchField('first_name'),
        index.SearchField('last_name'),
        index.SearchField('biography', partial_match=True),
    )

    panels = [
        MultiFieldPanel([
            FieldPanel('first_name'),
            FieldPanel('last_name'),
            FieldPanel('role'),
        ], "Name and Role"),
        ImageChooserPanel('photo'),
        PageChooserPanel('production', 'productions.ProductionPage'),
        FieldPanel('biography', classname="full"),
        MultiFieldPanel([
            FieldPanel('email'),
            FieldPanel('twitter_url'),
            FieldPanel('instagram_url'),
        ], "Contact")
    ]

    # TODO about.TeamPage?
    #parent_page_types = ['productions.PeopleIndexPage']
    #subpage_types = []

    class Meta:
        verbose_name = "person"
        verbose_name_plural = "people"

    def __str__(self):
        return "%s %s" % (
            self.first_name, self.last_name
        )
