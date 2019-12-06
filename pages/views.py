from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from products.models import Product
from products.forms import ProductForm


# Create your views here.
def home_view(request):
    my_context = {
        'my_text': 'This is my text.',
        'my_number': 123,
        'my_list': [1, 3, 5, 6, 7, 8, 8, 6, 5],
        'my_html': '<h1>This is my html<h1>',
        'my_products': Product.objects.all(),
    }

    return render(request, 'home.html', my_context)


def products_view(request):
    my_context = {
        'products': Product.objects.all()
    }
    return render(request, 'products.html', my_context)


def products_detail_view(request):
    obj = Product.objects.get(id=1)

    my_context = {'obj': obj}
    return render(request, 'detail.html', my_context)


def create_view(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ProductForm()

    my_context = {
        'form': form
    }
    return render(request, 'create.html', my_context)


def contact_view(*args, **kwargs):
    return HttpResponse('<h1>Hello World</h1>')
