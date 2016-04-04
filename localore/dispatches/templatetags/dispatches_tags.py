from django import template
#from dispatches.models import DispatchPage

register = template.Library()


#@register.inclusion_tag('dispatches/tags/menu.html', takes_context=True)
#def dispatches_menu(context):
#    for item in DispatchesPage.dispatch_types:
#        item.active = (
#            calling_page.url.startswith(item.url) if calling_page else False
#        )
#
#    return {
#        'menuitems': menuitems,
#        'request': context['request'],
#    }
