from django.db import models
from wagtail.contrib.settings.models import BaseSetting, register_setting
from wagtail.wagtailadmin.edit_handlers import FieldPanel


@register_setting(icon='site')
class JuicerSettings(BaseSetting):
    juicer_feed_id = models.CharField(
        max_length=200,
        help_text="Your Juicer feed ID."
    )
    juicer_auth_token = models.CharField(
        max_length=200,
        help_text="Your Juicer API authentication token."
    )

    panels = [
        FieldPanel('juicer_feed_id'),
        FieldPanel('juicer_auth_token'),
    ]
