from urllib.error import HTTPError
from urllib.request import Request, urlopen

from django.conf import settings

from wagtail.wagtailcore import hooks
from wagtail.wagtailadmin.site_summary import SummaryItem

import json
import logging


logger = logging.getLogger('localore.juicer_site_summary')


class JuicerSummaryItem(SummaryItem):
    order = 400
    template = 'localore_admin/site_summary_juicer.html'

    # TODO cache
    def get_context(self):
        request = Request(
            'https://www.juicer.io/api/feeds/'
            '%s/moderated?authentication_token=%s&count=true' % (
                settings.JUICER_FEED_ID,
                settings.JUICER_AUTH_TOKEN
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
            count = json.loads(r.read().decode('utf-8'))['posts']['total_count']
        except KeyError as err:
            logger.error("KeyError fetching Juicer post counts: %s", err)
            return {
                'error': True
            }

        return {
            'feed_id': settings.JUICER_FEED_ID,
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
