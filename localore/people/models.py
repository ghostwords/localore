from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from wagtail.wagtailadmin.edit_handlers import (
    FieldPanel,
    MultiFieldPanel,
    PageChooserPanel,
)
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from wagtail.wagtailsearch import index
from wagtail.wagtailsnippets.models import register_snippet

from productions.models import ProductionPageRelatedPerson


@register_snippet
class Person(models.Model, index.Indexed):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    role = models.CharField(max_length=255, blank=True)

    photo = models.ForeignKey(
        'localore_admin.LocaloreImage',
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

    biography = RichTextField(blank=True)

    email = models.EmailField(blank=True)
    twitter_url = models.URLField("Twitter URL", blank=True)
    instagram_url = models.URLField("Instagram URL", blank=True)

    # Wagtail search
    search_fields = (
        index.SearchField('first_name'),
        index.SearchField('last_name'),
    )

    # Wagtail admin
    panels = [
        MultiFieldPanel([
            FieldPanel('first_name'),
            FieldPanel('last_name'),
            ImageChooserPanel('photo'),
        ], "Name and Photo"),
        MultiFieldPanel([
            PageChooserPanel('production', 'productions.ProductionPage'),
            FieldPanel('role'),
        ], "Production"),
        FieldPanel('biography', classname="full"),
        MultiFieldPanel([
            FieldPanel('email'),
            FieldPanel('twitter_url'),
            FieldPanel('instagram_url'),
        ], "Contact")
    ]

    @property
    def full_name(self):
        return self.first_name + " " + self.last_name

    @property
    def role_and_production(self):
        if self.role and self.production:
            return self.role + ", " + self.production.title
        elif self.role:
            return self.role
        elif self.production:
            return self.production

    class Meta:
        ordering = ('last_name',)
        verbose_name = "Team Member"

    def __str__(self):
        out = [
            self.first_name,
            self.last_name
        ]

        if self.role_and_production:
            out.append("(%s)" % self.role_and_production)

        return " ".join(out)


@receiver(post_save, sender=Person)
# pylint: disable=unused-argument
def update_production_related_people(sender, instance, **kwargs):
    if not instance.production:
        return

    latest_revision = instance.production.get_latest_revision_as_page()

    related_people = [
        item.person for item in latest_revision.related_people.all()
    ]
    if instance in related_people:
        return

    latest_revision.related_people.add(ProductionPageRelatedPerson(
        page=instance.production,
        person=instance
    ))

    latest_revision.save_revision(
        user=instance.production.get_latest_revision().user
    )
