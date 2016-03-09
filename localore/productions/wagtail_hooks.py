from wagtailmodeladmin.options import ModelAdmin, wagtailmodeladmin_register
from .models import ProductionPage


class ProductionsAdmin(ModelAdmin):
    model = ProductionPage
    menu_icon = 'site'
    menu_label = 'Productions'
    menu_order = 200
    list_display = ('title', 'city', 'state')
    search_fields = ('title', 'description', 'highlights')

wagtailmodeladmin_register(ProductionsAdmin)
