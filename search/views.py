#from django.db.models import Q
from django.shortcuts import render
from products.models import Product


def search_product_view(request):

    method_dict = request.GET
    query = method_dict.get('q', None)
    if query is not None:
        #lookups =Q(title__icontains=query) | Q(description__icontains=query)
        #queryset = Product.objects.filter(lookups).distinct()
        queryset= Product.objects.search(query)
    else :
        queryset = Product.objects.featured()
    context = {
        "q": queryset,
    }
    print(query)
    return render(request, "search/view.html", context)