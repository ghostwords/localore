from django.contrib.contenttypes.models import ContentType
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.cache import cache_page

from wagtail.wagtailcore.models import Page
from wagtail.wagtailsearch.models import Query

from localore_admin.models import PageAlias


# override per-site cache for search
@cache_page(30) # thirty seconds
def search(request):
    do_json = 'json' in request.GET
    search_query = request.GET.get('query', None)
    page = request.GET.get('page', 1)

    # Search
    if search_query:
        page_alias_content_type = ContentType.objects.get_for_model(PageAlias)

        search_results = (
            Page.objects.live()
            # exclude root and home pages
            .filter(depth__gt=2)
            # exclude PageAlias pages
            .exclude(content_type=page_alias_content_type)
            .search(search_query)
        )

        # log the query so Wagtail can suggest promoted results
        Query.get(search_query).add_hit()
    else:
        search_results = Page.objects.none()

    # Pagination
    paginator = Paginator(search_results, 10)
    try:
        search_results = paginator.page(page)
    except PageNotAnInteger:
        search_results = paginator.page(1)
    except EmptyPage:
        search_results = paginator.page(paginator.num_pages)

    response = {
        'search_query': search_query,
        'search_results': search_results,
    }

    if do_json:
        search_results_serializable = []

        for res in response['search_results']:
            res_serializable = {}

            res_serializable['title'] = res.specific.title
            res_serializable['url'] = res.specific.url
            res_serializable['content_type'] = res.specific.content_type.name

            search_results_serializable.append(res_serializable)

        response['search_results'] = search_results_serializable

        return JsonResponse(response)

    else:
        return render(request, 'search/search.html', response)
