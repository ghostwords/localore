from django.utils.html import format_html
from django.conf import settings

from wagtail.wagtailcore import hooks

@hooks.register('insert_editor_css')
def editor_css():
    return format_html('<link rel="stylesheet" href="{0}'
        'css/admin-streamfield-styles.css">'.format(settings.STATIC_URL))
