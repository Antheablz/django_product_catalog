from django.shortcuts import render
from .models import Category, Tag, Product


# Create your views here.
def home(request):
    '''
    Renders the home page with filtered product listings and catalog data.

    Fetches all available categories and tags to build the sidebar filters,
    then filters the product catalog based on search keywords, selected 
    categories, and selected tags passed through the URL query parameters.

    Args:
        request (HttpRequest): The incoming HTTP request object.

    Returns:
        HttpResponse: A fully rendered HTML page using the 'index.html' template.
    '''
    categories = Category.objects.all()
    tags = Tag.objects.all()
    products = Product.objects.all()

    search = request.GET.get("search")
    category = request.GET.getlist("category")
    tag = request.GET.getlist("tag")

    if search:
        products = products.filter(description__icontains=search)

    if category:
        products = products.filter(category__name__in=category)

    if tag:
        products = products.filter(tags__name__in=tag)

    context = {
        "categories": categories,
        "tags": tags,
        "products": products,
        "selected_categories": category,
        "selected_tags": tag,
        "selected_search": search
    }

    return render(request, 'index.html', context)