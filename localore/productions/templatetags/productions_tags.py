from django import template
from productions.models import ProductionsIndexPage, ProductionPage

register = template.Library()


@register.assignment_tag
def get_productions_index_page():
    return ProductionsIndexPage.objects.live().first()


@register.inclusion_tag(
    'productions/tags/productions.html',
    takes_context=True
)
def productions(context):
    return {
        'productions': ProductionPage.objects.live(),
        'request': context['request'],
    }
