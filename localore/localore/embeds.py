from urllib.parse import urlparse

from django.conf import settings

from wagtail.wagtailembeds.finders.embedly import embedly
from wagtail.wagtailembeds.finders.oembed import oembed


def get_default_finder():
    if hasattr(settings, 'WAGTAILEMBEDS_EMBEDLY_KEY'):
        return embedly
    return oembed


def finder(url, max_width=None):
    domain = urlparse(url).netloc

    # work around Embedly missing embedding HTML for Twitter and Instagram URLs
    if domain.endswith((
        'instagram.com',
        'twitter.com',
    )):
        return oembed(url, max_width)

    embed_dict = get_default_finder()(url, max_width)

    if domain.endswith('soundcloud.com'):
        embed_dict['html'] = (
            embed_dict['html']
            .replace('visual%3Dtrue', 'visual%3Dfalse')
            .replace('width="500"', 'width="100%"')
            .replace('height="500"', 'height="166"')
        )
        embed_dict['width'] = '100%'
        embed_dict['height'] = '166'

    return embed_dict
