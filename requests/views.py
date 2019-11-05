from django.shortcuts import render, redirect
from .forms import RequestsForm
from products.models import Product
from .models import Requests, friend_request
from django.contrib import messages
from accounts.models import User
from django.core.mail import send_mail
from userprofile.models import Userprofile



def requests_home(request) :
    user = request.user
    product_id = request.POST.get('product')
    product = Product.objects.get(id=product_id)
    # if p2 is selected it will give error
    #p2 = Product.objects.get(id=product_id)
    #print(product)
    #print(p2)
    user= Product.objects.get_userp_by_title(product.title)
    owner = User.objects.get(id=user.id)
    user = request.user
    #requests_form = RequestsForm(request.POST or None)
    context = {
        #'form' : requests_form,
        'product' : product,


    }
    status='accepted'
    new_req = Requests.objects.create_request(user,product,'accepted')
    messages.success(request, "Request sent successfully")
    # send_mail(
    #     'TaskShare',
    #     'The details of your task are written below',
    #     'shaad.sufi@ug.bilkent.edu.tr',
    #     [user.email],
    #     fail_silently=False,
    # )

    #context = {}


    return render(request,'requests/home.html', context)

def friend_request(request) :
    sender = request.user
    next = request.POST.get('next', '/')
    slug_reciever = str(next)[9:-1]
    userprofile = Userprofile.objects.filter(slug=slug_reciever)
    reciever = userprofile[0].user
    Requests.objects.create_friend_request(sender,reciever)
    messages.success(request, "Friend request sent successfully")



    return redirect('/profile/' + slug_reciever)

