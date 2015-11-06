from wagtail.wagtailcore import hooks
from wagtail.wagtailadmin.site_summary import SummaryItem


class JuicerSummaryItem(SummaryItem):
    order = 400
    template = 'localore_admin/site_summary_juicer.html'

    def get_context(self):
        return {
            # TODO total Juicer posts (awaiting moderation?)
            'total_posts': 0
        }


@hooks.register('construct_homepage_summary_items')
def add_juicer_summary_item(request, items):
    # remove wagtaildocs' page summary
    items[:] = [
        item for item in items
        if item.__class__.__name__ not in ('DocumentsSummaryItem')
    ]
    items.append(JuicerSummaryItem(request))
