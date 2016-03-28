from django import template

register = template.Library()


@register.inclusion_tag(
    'people/tags/person.html',
    takes_context=True
)
def person(context, person_model):
    return {
        'person': person_model,
        'request': context['request'],
    }
