from django import template

from localore_admin.models import PageAlias

register = template.Library()


@register.assignment_tag
def get_dispatches_index_page():
    # TODO make more robust
    return PageAlias.objects.live().filter(title="Dispatches").first()
