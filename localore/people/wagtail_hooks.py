from wagtailmodeladmin.options import ModelAdmin, wagtailmodeladmin_register
from .models import Person


class PeopleAdmin(ModelAdmin):
    model = Person
    menu_icon = 'user'
    menu_label = 'Localore Team'
    menu_order = 200 # put in 3rd place (000 being 1st, 100 2nd)
    list_display = ('first_name', 'last_name', 'production', 'role')
    list_filter = ('role', 'production')
    search_fields = ('first_name', 'last_name', 'biography')

wagtailmodeladmin_register(PeopleAdmin)
