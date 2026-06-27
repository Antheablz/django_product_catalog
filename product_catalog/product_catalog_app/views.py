from django.shortcuts import render
from .models import Category, Tag, Product

# Create your views here.
def home(request):
    categories = Category.objects.all()
    tags = Tag.objects.all()
    products = Product.objects.all()

    search = request.GET.get("search")
    category = request.GET.get("category")
    tag = request.GET.get("tag")

    if search:
        products = products.filter(description__icontains=search)

    if category:
        products = products.filter(category__name=category)

    if tag:
        products = products.filter(tags__name=tag)

    context = {
        "categories": categories,
        "tags": tags,
        "products": products
    }
    return render(request, 'index.html', context)