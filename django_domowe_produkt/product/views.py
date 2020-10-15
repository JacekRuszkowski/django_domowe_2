from django.shortcuts import render, get_object_or_404
from .models import Product
from django.views.generic import (
    UpdateView,
    CreateView,
    DeleteView
)

# Create your views here.


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'product/product.html', {'product': product})


def home(request):
    content = {'all_products': Product.objects.all()}
    return render(request, 'product/home.html', content)


class EditProduct(UpdateView):
    model = Product
    fields = ['title', 'description', 'price', 'is_available']


class AddProduct(CreateView):
    model = Product
    fields = ['title', 'description', 'price', 'is_available']

class DeleteProduct(DeleteView):
    model = Product
    success_url = '/'


"""
Dorobić przycisk edytuj.
Po kliknięciu, jeśłi niezalogowany przenosi na stronę logowania.
Jeśli zalogowany przenosi na stronę admina. 
Czy mogę zrobić swój widok admina django?

"""