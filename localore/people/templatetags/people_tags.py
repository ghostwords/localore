from django import template
from people.models import Person

register = template.Library()


@register.inclusion_tag('people/tags/people.html', takes_context=True)
def people(context):
    return {
        'people': Person.objects.all(),
        'request': context['request'],
    }
