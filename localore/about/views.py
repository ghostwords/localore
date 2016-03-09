from django.shortcuts import render


def about(request, current_page_name, about_page_names):
    return render(
        request,
        'about/' + current_page_name + '.html',
        {
            'current_page_name': current_page_name,
            'about_page_names': about_page_names
        }
    )
