from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth import login
from .forms import ContactForm
from requests.models import Requests

def home_page(request):
    print(request.session.get('first_name','Unknown'))
    print (request.session.get('cart_id'))
    context = {
        "title" : "BilShare",
        "intro" : "This is the home page",
        'username' : request.session.get('first_name','Unknown')
    }
    if request.user.is_authenticated():
        context["premium_content"]  = "The content on this page is exclusive to this user"

    return render(request,"home_page.html", context)
def about_page(request):
    context = {
        "title": "About",
        "intro": "This is the about page",
    }
    return render(request, "home_page.html", context)

def contact_page(request):
    contact_form = ContactForm(request.POST or None)
    context = {
        "title": "Contact",
        "intro": "This is the con tact page",
        "form":   contact_form,
        "brand" : "New Brand Name"
    }
    if contact_form.is_valid():
        print(contact_form.cleaned_data)

    return render(request, "contact/view.html", context)


def my_orders(request):
    user = request.user
    orders = Requests.objects.filter(user = user)[::-1]
    print(orders)
    context = {
        'orders':orders
    }
    #print(orders)
    return render(request,"my_orders.html", context)
