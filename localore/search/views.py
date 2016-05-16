from django.contrib.contenttypes.models import ContentType
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import JsonResponse
from django.shortcuts import render
from django.template import defaultfilters

from wagtail.wagtailcore.models import Page
from wagtail.wagtailsearch.backends import get_search_backend
from wagtail.wagtailsearch.models import Query

from about.models import AboutTeamPage
from localore_admin.models import PageAlias
from people.models import Person


def get_results_json(response):
    results_json = {
        'search_query': response['search_query'],
        'search_results': [],
    }

    for result_type in ('promoted_results', 'search_results'):
        for page in response[result_type]:
            page = page.specific
            result = {}

            result['title'] = page.title
            result['url'] = page.url

            # if page is an index page, blank out the content type
            if page.content_type.name.endswith('Index'):
                content_type = "&nbsp;"
            else:
                parent = Page.objects.parent_of(page).first()
                # if page is a child of an index page
                if (
                    parent and
                    parent.specific.content_type.name.endswith('Index')
                ):
                    # use the parent's title for content type
                    content_type = parent.title
                else:
                    content_type = page.content_type.name
            result['content_type'] = content_type

            if result not in results_json['search_results']:
                results_json['search_results'].append(result)

    about_team_page = AboutTeamPage.objects.live().first()
    for person in response['people_results']:
        results_json['search_results'].append({
            'content_type': about_team_page.title,
            'title': str(person),
            'url': '%s#%s-%s' % (
                about_team_page.url,
                defaultfilters.slugify(person.full_name),
                person.pk
            ),
        })

    return results_json


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

        query = Query.get(search_query)

        # log the query so Wagtail can suggest promoted results
        query.add_hit()

        # promoted search results
        promoted_page_ids = [
            pick.page.id for pick in query.editors_picks.all()
        ]
        promoted_results = Page.objects.filter(pk__in=promoted_page_ids)

        # search Person snippets
        search_backend = get_search_backend()
        people_results = search_backend.search(
            search_query, Person.objects.all()
        )
    else:
        search_results = Page.objects.none()
        promoted_results = Page.objects.none()
        people_results = Person.objects.none()

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
        'promoted_results': promoted_results,
        'people_results': people_results,
    }

    if do_json:
        return JsonResponse(get_results_json(response))
    else:
        return render(request, 'search/search.html', response)
