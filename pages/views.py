from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def home_view(request):
    return render(request, 'home.html')


def contact_view(*args, **kwargs):
    return HttpResponse('<h1>Hello World</h1>')


def products_view(*args, **kwargs):
    return HttpResponse('<h1>Hello World</h1>')
