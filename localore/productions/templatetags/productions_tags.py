from django import template
from productions.models import ProductionsIndexPage

register = template.Library()


@register.assignment_tag
def get_productions_index_page():
    return ProductionsIndexPage.objects.live().first()
