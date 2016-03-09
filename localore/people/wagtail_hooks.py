from wagtailmodeladmin.options import ModelAdmin, wagtailmodeladmin_register
from .models import Person


class PeopleAdmin(ModelAdmin):
    model = Person
    menu_icon = 'group'
    menu_label = 'Team'
    menu_order = 300
    list_display = ('full_name', 'production', 'role')
    list_filter = ('role', 'production')
    ordering = ('-production',)
    search_fields = ('last_name', 'first_name', 'biography')

    # pylint: disable=no-self-use
    def full_name(self, obj):
        return "%s %s" % (
            obj.first_name,
            obj.last_name
        )
    full_name.short_description = 'name'
    full_name.admin_order_field = 'last_name'

wagtailmodeladmin_register(PeopleAdmin)
