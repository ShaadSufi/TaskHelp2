from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, get_user_model,login
from django.utils.http import is_safe_url
from .forms import LoginForm,RegisterForm,GuestForm
from django.contrib.auth import logout
from django.contrib import messages
from .models import GuestEmail
from products.models import Product
from django.conf import settings

def guest_register_view(request):
    guest_form = GuestForm(request.POST or None)
    context = {

        "title" : "Guest Login",
        "form": guest_form
    }
    next_ = request.GET.get('next')
    next_post = request.POST.get('next')
    redirect_path = next_ or next_post or None

    if guest_form.is_valid():
        email = guest_form.cleaned_data.get("email")
        new_guest_email = GuestEmail.objects.create(email=email)
        request.session['guest_email_id'] = new_guest_email.id
        if is_safe_url(redirect_path, request.get_host()):
            return redirect(redirect_path)
        else:
            return redirect("/register/")

    return redirect("/register/")


def login_page(request):
    login_form = LoginForm(request.POST or None)
    context = {

        "title" : "Login",
        "form": login_form
    }
    next_ = request.GET.get('next')
    next_post = request.POST.get('next')
    redirect_path = next_ or next_post or None

    if login_form.is_valid():
        print(login_form.cleaned_data)
        username = login_form.cleaned_data.get("username")
        password = login_form.cleaned_data.get("password")
        user = authenticate( username=username, password=password)
        if user is not None:
            login(request, user)
            try :
                del request.session['guest_email_id']
            except:
                pass
            if is_safe_url(redirect_path, request.get_host()):
                return redirect(redirect_path)
            else:
                context['form'] = LoginForm()
                return redirect("/")
        else:
            print("Error")

    return render(request, "accounts/login_page.html", context)

User = get_user_model()

def register_page(request):
    register_form = RegisterForm(request.POST or None)
    context = {

        "title" : "Register",
        "form": register_form
    }
    if register_form.is_valid():
      register_form.save()
    #return render(request, "products/list.html", context)
    return render(request, "accounts/register_page.html", context)



def logout_view(request):
    logout(request)
    return redirect('/login/')

user = settings.AUTH_USER_MODEL
# def my_profile(request):
#     context = {}
#     return render(request,'accounts/myprofile.html', context)
# def product_requests(request):
#     context = {}
#     return render(request, 'accounts/product_requests.html', context)
# def my_products(request):
#     user = request.user
#     products = Product.objects.get_by_user(user)
#     context = {
#         'products' : products
#     }
#     return render(request,'accounts/my_products.html', context)
# def favorites(request):
#     context = {}
#     return render(request,'accounts/favorites.html', context)
# def sentrequests(request):
#     context = {}
#     return render(request,'accounts/sentrequests.html', context)
# def recievedrequests(request):
#
#     context = {}
#     return render(request,'accounts/recievedrequests.html',context)