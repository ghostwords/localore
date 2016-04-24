from django import template
from dispatches.models import DISPATCH_TYPE_CHOICES

register = template.Library()


@register.inclusion_tag('dispatches/tags/menu.html', takes_context=True)
def dispatches_menu(context, index_page, dispatch_type):
    menuitems = []

    for (value, name) in DISPATCH_TYPE_CHOICES:
        item = {}

        item['name'] = name
        item['value'] = value
        item['active'] = (
            context['request'].GET.get('t', dispatch_type) == value
        )

        menuitems.append(item)

    return {
        'index_page': index_page,
        'menuitems': menuitems,
        'request': context['request'],
    }
