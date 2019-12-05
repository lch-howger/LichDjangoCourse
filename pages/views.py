from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from products import models


# Create your views here.
def home_view(request):
    my_context = {
        'my_text': 'This is my text.',
        'my_number': 123,
        'my_list': [1, 3, 5, 6, 7, 8, 8, 6, 5],
        'my_html': '<h1>This is my html<h1>',
    }

    return render(request, 'home.html', my_context)


def contact_view(*args, **kwargs):
    return HttpResponse('<h1>Hello World</h1>')


def products_view(*args, **kwargs):
    return HttpResponse('<h1>Hello World</h1>')
