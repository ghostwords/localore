from django.core.urlresolvers import reverse
from django.utils.html import format_html

from wagtailmodeladmin.options import ModelAdmin, wagtailmodeladmin_register

from people.models import Person


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

    def profile_photo(self, obj):
        if not obj.photo:
            return
        return format_html(
            '<img src="{}" title="{}" alt="{}" style="height:40px">',
            obj.photo.file.url,
            obj.photo,
            "team member profile photo of " + self.full_name(obj)
        )
    profile_photo.short_description = 'photo'

wagtailmodeladmin_register(PeopleAdmin)
