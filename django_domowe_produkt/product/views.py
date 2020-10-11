from django.shortcuts import render, get_object_or_404
from .models import Product

# Create your views here.



def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'product/product.html', {'product': product})

def home(request):
    content = {'all_products': Product.objects.all()}
    return render(request, 'product/home.html', content)

def redirect_edit(request):
    return render(request, 'product/edit.html')



"""
Dorobić przycisk edytuj.
Po kliknięciu, jeśłi niezalogowany przenosi na stronę logowania.
Jeśli zalogowany przenosi na stronę admina. 
Czy mogę zrobić swój widok admina django?

"""