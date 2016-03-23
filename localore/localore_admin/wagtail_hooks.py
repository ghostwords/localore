from django.conf.urls import url

from wagtail.wagtailcore import hooks
from wagtail.wagtailadmin.site_summary import SummaryItem

from localore_admin import views


class JuicerSummaryItem(SummaryItem):
    order = 400
    template = 'localore_admin/site_summary_juicer.html'


@hooks.register('construct_homepage_summary_items')
def add_juicer_summary_item(request, items):
    # remove wagtaildocs' page summary
    items[:] = [
        item for item in items
        if item.__class__.__name__ != 'DocumentsSummaryItem'
    ]

    items.append(JuicerSummaryItem(request))


@hooks.register('register_admin_urls')
def juicer_summary_item():
    return [
        url(
            r'^juicer-summary-item/$',
            views.juicer_summary_item,
            name='localore-admin-juicer-summary-item'
        ),
    ]


@hooks.register('construct_main_menu')
def hide_snippets_menu_item(_, menu_items):
    menu_items[:] = [item for item in menu_items if item.name != 'snippets']
