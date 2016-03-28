from urllib.parse import urlparse

from django.conf import settings

from wagtail.wagtailembeds.finders.embedly import embedly
from wagtail.wagtailembeds.finders.oembed import oembed


# work around Embedly missing embedding HTML for Twitter and Instagram URLs
def finder(url, max_width=None):
    domain = urlparse(url).netloc
    if (domain.endswith(('instagram.com', 'twitter.com')) or
            not hasattr(settings, 'WAGTAILEMBEDS_EMBEDLY_KEY')):
        return oembed(url, max_width)

    return embedly(url, max_width)
