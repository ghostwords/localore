from django import template
from dispatches.models import DISPATCH_TYPE_CHOICES

register = template.Library()


@register.inclusion_tag('dispatches/tags/menu.html', takes_context=True)
def dispatches_menu(context, calling_page):
    menuitems = []

    for (value, name) in DISPATCH_TYPE_CHOICES:
        item = {}

        item['name'] = name
        item['value'] = value
        item['active'] = context['request'].GET.get(
            't', calling_page.default_dispatch_type
        ) == value

        menuitems.append(item)

    return {
        'page': calling_page,
        'menuitems': menuitems,
        'request': context['request'],
    }
