from django.utils.html import format_html

from wagtailmodeladmin.options import ModelAdmin, wagtailmodeladmin_register

from .models import Person


class PeopleAdmin(ModelAdmin):
    model = Person
    menu_icon = 'group'
    menu_label = 'Team'
    menu_order = 300
    list_display = ('profile_photo', 'full_name', 'production', 'role')
    list_filter = ('role', 'production')
    search_fields = ('last_name', 'first_name', 'biography')

    def full_name(self, obj): # pylint: disable=no-self-use
        return "%s %s" % (
            obj.first_name,
            obj.last_name
        )
    full_name.short_description = 'name'
    full_name.admin_order_field = 'last_name'

    def profile_photo(self, obj):
        return format_html(
            '<img src="{}" title="{}" alt="{}" style="height:40px">',
            obj.photo.file.url,
            obj.photo,
            "team member profile photo of " + self.full_name(obj)
        )
    profile_photo.allow_tags = True
    profile_photo.short_description = 'photo'

wagtailmodeladmin_register(PeopleAdmin)
