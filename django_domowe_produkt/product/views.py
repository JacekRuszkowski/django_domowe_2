from django.shortcuts import render
from .models import Product

# Create your views here.


def product_view(request):
    content = {'product': Product.objects.first()}
    return render(request, 'product/product.html', content)


def home(request):
    content = {'all_products': Product.objects.all()}
    return render(request, 'product/home.html', content)