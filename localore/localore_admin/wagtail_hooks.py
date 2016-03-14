import json
import logging

from urllib.error import HTTPError
from urllib.request import Request, urlopen

from wagtail.wagtailcore import hooks
from wagtail.wagtailadmin.site_summary import SummaryItem

from localore_admin.models import JuicerSettings


logger = logging.getLogger('localore.juicer_site_summary')


class JuicerSummaryItem(SummaryItem):
    order = 400
    template = 'localore_admin/site_summary_juicer.html'

    # TODO cache
    def get_context(self):
        settings = JuicerSettings.for_site(self.request.site)
        if not settings.juicer_feed_id or not settings.juicer_auth_token:
            return {
                'error': True,
                'settings_error': True
            }

        request = Request(
            'https://www.juicer.io/api/feeds/'
            '%s/moderated?authentication_token=%s&count=true' % (
                settings.juicer_feed_id,
                settings.juicer_auth_token
            )
        )
        try:
            r = urlopen(request)
        except HTTPError as err:
            logger.error("HTTPError fetching Juicer post counts: %s", err)
            return {
                'error': True
            }

        try:
            count = json.loads(
                r.read().decode('utf-8')
            )['posts']['total_count']
        except KeyError as err:
            logger.error("KeyError fetching Juicer post counts: %s", err)
            return {
                'error': True
            }

        return {
            'feed_id': settings.juicer_feed_id,
            'total_posts': count
        }


@hooks.register('construct_homepage_summary_items')
def add_juicer_summary_item(request, items):
    # remove wagtaildocs' page summary
    items[:] = [
        item for item in items
        if item.__class__.__name__ not in ('DocumentsSummaryItem')
    ]

    items.append(JuicerSummaryItem(request))


@hooks.register('construct_main_menu')
def hide_snippets_menu_item(_, menu_items):
    menu_items[:] = [item for item in menu_items if item.name != 'snippets']
