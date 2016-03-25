from django.core.urlresolvers import reverse
from django.utils.html import format_html

from wagtail.wagtailadmin.search import SearchArea
from wagtail.wagtailcore import hooks
from wagtail.wagtailsnippets.permissions import user_can_edit_snippet_type

from wagtailmodeladmin.options import (
    ModelAdmin,
    ThumbmnailMixin,
    wagtailmodeladmin_register
)

from people.models import Person


class PeopleSearchArea(SearchArea):
    def is_shown(self, request):
        return user_can_edit_snippet_type(request.user, Person)


@hooks.register('register_admin_search_area')
def register_people_search_area():
    return PeopleSearchArea(
        'Team Members',
        reverse('people_person_modeladmin_index/'),
        classnames='icon icon-group',
        order=150
    )


class PersonThumbnailMixin(ThumbmnailMixin):
    thumb_image_field_name = 'photo'


class PeopleAdmin(ModelAdmin):
    model = Person
    menu_icon = 'group'
    menu_label = 'Team'
    menu_order = 300
    list_display = ('profile_photo', 'full_name', 'role_and_production')
    list_filter = ('role', 'production')
    search_fields = (
        'first_name',
        'last_name',
        'role',
        'biography',
        'production__title',
    )

    def profile_photo(self, obj): # pylint: disable=no-self-use
        return PersonThumbnailMixin().admin_thumb(obj)
    profile_photo.short_description = "photo"

    def role_and_production(self, obj): # pylint: disable=no-self-use
        if obj.production and obj.role:
            return format_html(
                '{} at <a href="{}">{}</a>',
                obj.role,
                reverse('wagtailadmin_pages:edit', args=(obj.production.id,)),
                obj.production
            )
        elif obj.production:
            return format_html(
                '<a href="{}">{}</a>',
                reverse('wagtailadmin_pages:edit', args=(obj.production.id,)),
                obj.production
            )
        elif obj.role:
            return obj.role
        else:
            return ""
    role_and_production.admin_order_field = '-production'

    def full_name(self, obj): # pylint: disable=no-self-use
        return "%s %s" % (
            obj.first_name,
            obj.last_name
        )
    full_name.short_description = 'name'
    full_name.admin_order_field = 'last_name'

wagtailmodeladmin_register(PeopleAdmin)
