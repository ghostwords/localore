from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import JsonResponse
from django.shortcuts import render

from wagtail.wagtailcore.models import Page
from wagtail.wagtailsearch.models import Query


def search(request):
    do_json = 'json' in request.GET
    search_query = request.GET.get('query', None)
    page = request.GET.get('page', 1)

    # Search
    if search_query:
        search_results = Page.objects.live().search(search_query)
        query = Query.get(search_query)

        # Record hit
        query.add_hit()
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
