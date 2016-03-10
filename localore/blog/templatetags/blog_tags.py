from django import template
from blog.models import BlogIndexPage

register = template.Library()


@register.assignment_tag
def get_blog_index_page():
    return BlogIndexPage.objects.live().first()
