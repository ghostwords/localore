from django import template
from django.db.models import Q

from people.models import Person

register = template.Library()


@register.inclusion_tag('people/tags/people.html', takes_context=True)
def people(context):
    return {
        'people': Person.objects.filter(
            Q(production__live=True) | Q(production__isnull=True)
        ),
        'request': context['request'],
    }
