from django import template

from home.models import HomePage

register = template.Library()


@register.assignment_tag
def get_menu_items():
    return HomePage.objects.live().first().get_children().live().in_menu()
