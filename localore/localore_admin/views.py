import json
import logging

from urllib.error import HTTPError
from urllib.request import Request, urlopen

from django.shortcuts import render

from localore_admin.models import JuicerSettings


logger = logging.getLogger('localore.juicer_site_summary')


def get_juicer_count(settings):
    if not settings.juicer_feed_id or not settings.juicer_auth_token:
        return {
            'error': True,
            'settings_error': True
        }

    http_request = Request(
        'https://www.juicer.io/api/feeds/'
        '%s/moderated?authentication_token=%s&count=true' % (
            settings.juicer_feed_id,
            settings.juicer_auth_token
        )
    )
    try:
        http_response = urlopen(http_request)
    except HTTPError as err:
        logger.error("HTTPError fetching Juicer post counts: %s", err)
        return {
            'error': True
        }

    try:
        count = json.loads(
            http_response.read().decode('utf-8')
        )['posts']['total_count']
    except KeyError as err:
        logger.error("KeyError fetching Juicer post counts: %s", err)
        return {
            'error': True
        }

    # TODO cache
    return {
        'feed_id': settings.juicer_feed_id,
        'total_posts': count
    }


def juicer_summary_item(request):
    settings = JuicerSettings.for_site(request.site)

    return render(
        request,
        'localore_admin/juicer_summary_item.html',
        get_juicer_count(settings)
    )
