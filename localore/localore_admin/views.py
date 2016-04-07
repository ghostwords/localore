import json
import logging

from urllib.error import HTTPError
from urllib.request import Request, urlopen

from django.core.cache import cache
from django.shortcuts import render

from localore_admin.models import JuicerSettings


logger = logging.getLogger('localore.juicer_site_summary')


def get_juicer_count(settings):
    feed_id = settings.juicer_feed_id
    auth_token = settings.juicer_auth_token
    cache_key = 'localore.juicer_feed.' + feed_id + '.count'

    if not feed_id or not auth_token:
        return {
            'error': True,
            'settings_error': True
        }

    # see if we have the count in cache
    count = cache.get(cache_key)
    if count is not None:
        return {
            'feed_id': feed_id,
            'total_posts': count
        }

    http_request = Request(
        'https://www.juicer.io/api/feeds/%s/moderated?'
        'authentication_token=%s&count=true' % (
            feed_id, auth_token
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

    # cache the non-error result
    cache.set(cache_key, count, 600) # ten minutes

    return {
        'feed_id': feed_id,
        'total_posts': count
    }


def juicer_summary_item(request):
    settings = JuicerSettings.for_site(request.site)

    return render(
        request,
        'localore_admin/juicer_summary_item.html',
        get_juicer_count(settings)
    )
