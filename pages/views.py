from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def home_view(request):
    my_context={
        'my_text':'This is my text.',
        'my_number': 123
    }
    return render(request, 'home.html',my_context)


def contact_view(*args, **kwargs):
    return HttpResponse('<h1>Hello World</h1>')


def products_view(*args, **kwargs):
    return HttpResponse('<h1>Hello World</h1>')
