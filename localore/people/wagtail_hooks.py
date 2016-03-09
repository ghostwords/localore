from wagtailmodeladmin.options import ModelAdmin, wagtailmodeladmin_register
from .models import Person


class PeopleAdmin(ModelAdmin):
    model = Person
    menu_icon = 'group'
    menu_label = 'Team'
    menu_order = 300
    list_display = ('first_name', 'last_name', 'production', 'role')
    list_filter = ('role', 'production')
    ordering = ('-production',)
    search_fields = ('first_name', 'last_name', 'biography')

wagtailmodeladmin_register(PeopleAdmin)
