from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.http.request import HttpRequest
from ecommerce.serializers.request_serializer import PastRequestSerializer
from ecommerce.error_handler import ResponseNotFound, ResponseNotAuth
from django.http.response import HttpResponse
from products.models import Product
from .models import Requests, REQUESTS_STATUS_CHOICES
from django.contrib import messages
from accounts.models import User
from userprofile.models import Userprofile


class PastRequests(TemplateView):
    # GET requests/past_request?offset={int}&limit={int}/
    def get(self, request: HttpRequest, *args, **kwargs):
        if request.user.is_authenticated():
            params = {
                'offset': int(request.GET.get('offset', 0)),
                'limit': int(request.GET.get('limit', 10))
            }
            reqs = Requests.objects.get_past_requests(user=request.user, **params)
            if reqs is not None and reqs:
                reqs_json = PastRequestSerializer.obj_list_to_dict_list(reqs).to_json()
                return HttpResponse(content=reqs_json, content_type='application/json', status=200)
            return ResponseNotFound(content={
                'errors': ['Empty query']
            })
        return ResponseNotAuth(content={
                'errors': ['User is not authorized']
            })

    # POST request/{id:int}/
    # UPDATING POST TO CANCEL
    def post(self, request: HttpRequest, id: str, *args, **kwargs):
        id = int(id)
        if request.user.is_authenticated():
            reqs = Requests.objects.get_past_request_by_id(user=request.user, _id=id)
            if reqs is not None and reqs:
                reqs.delete()
                reqs_json = PastRequestSerializer.from_db(reqs).to_dict().to_json()
                return HttpResponse(content=reqs_json, content_type='application/json', status=200)
        return ResponseNotAuth(content={
            'errors': ['User is not authorized']
        })


def requests_home(request) :
    user = request.user
    print(user)
    product_id = request.POST.get('product')
    product = Product.objects.get(id=product_id)
    # if p2 is selected it will give error
    #p2 = Product.objects.get(id=product_id)
    #print(product)
    #print(p2)
    # user= Product.objects.get_userp_by_title(product.title)
    #owner = User.objects.get(id=user.id)
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

