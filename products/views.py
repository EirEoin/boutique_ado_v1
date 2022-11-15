from django.shortcuts import render
from .models import Product

# Create your views here.

def all_produts(request):
    """ A view to show all products, including sorting and searching """

    return render(request, 'products/products.html', context)
