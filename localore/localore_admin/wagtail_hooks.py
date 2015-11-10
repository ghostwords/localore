from django.utils.six.moves.urllib import request as urllib_request
from django.utils.six.moves.urllib.request import Request

from wagtail.wagtailcore import hooks
from wagtail.wagtailadmin.site_summary import SummaryItem

import json


class JuicerSummaryItem(SummaryItem):
    order = 400
    template = 'localore_admin/site_summary_juicer.html'

    # TODO cache
    def get_context(self):
        request = Request(
            'https://www.juicer.io/api/feeds/'
            'fa-demo/moderated?authentication_token='
            'kGLT6vTEufYRz_csX8Ud&count=true'
        )
        r = urllib_request.urlopen(request)
        count = json.loads(r.read().decode('utf-8'))['posts']['total_count']

        return {
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
