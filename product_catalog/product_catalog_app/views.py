from django.shortcuts import render
from .models import Product

# Create your views here.
# def home(request):
#     return render(request, 'index.html')

def product_page(request):
    products = Product.objects.all()
    
    return render(request, 'index.html', {'products': products})