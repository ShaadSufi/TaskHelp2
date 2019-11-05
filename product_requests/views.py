from django.shortcuts import render
from .models import Product_Request
from django.conf import settings
from products.models import Product
# Create your views here.

User = settings.AUTH_USER_MODEL

def recievedrequest(request):
    requests = Product_Request.objects.all()
    context = {
        'requests': requests,
    }
    return render(request,'recieved_request.html',context)


def sentrequest(request):
    requests = Product_Request.objects.filter(sender = request.user)
    for request_ in requests:
        print(request_.product.user)
    context = {
    }
    return render(request,'product_requests/recieved_request.html',context)