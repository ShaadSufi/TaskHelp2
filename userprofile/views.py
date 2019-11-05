from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import get_user_model
from django.contrib import messages
from products.models import Product
from django.conf import settings
from requests.models import Requests, friend_request
from django.views.generic import DetailView
from .models import Userprofile
from django.http import Http404, HttpResponse, HttpResponseRedirect
from .forms import FriendRequestForm, EditProfileForm
from accounts.models import User



user = settings.AUTH_USER_MODEL
def my_profile(request):
    edit_profile_form = EditProfileForm(request.POST)

    context = {
        'form': edit_profile_form,
    }
    if edit_profile_form.is_valid():
        full_name = edit_profile_form.cleaned_data.get('full_name')
        phone = edit_profile_form.cleaned_data.get('phone')
        account = User.objects.filter( email = request.user.email)[0]
        profile = Userprofile.objects.filter( email = request.user.email)[0]

        account.full_name = full_name
        account.save()
        profile.full_name = full_name
        profile.phone= phone
        profile.save()

    return render(request,'userprofile/myprofile.html', context)
def task_requests(request):
    user = request.user
    req_qs = Requests.objects.get_by_user(user)
    new_req_qs = list(dict.fromkeys(req_qs))
    print(new_req_qs)
    context = {
        'object_qs': new_req_qs,
    }

    return render(request, 'userprofile/product_requests.html', context)

def my_tasks(request):
    user = request.user
    product_qs = Product.objects.get_by_userp(user)
    task_no_repitition_qs = []
    for object in product_qs:
        if object in task_no_repitition_qs==False:
            task_no_repitition_qs.append(object)

    context = {
        'object_qs' : task_no_repitition_qs,
    }
    return render(request,'userprofile/my_products.html', context)


def friend_requests(request):
    user = request.user

    friend_request_qs = friend_request.objects.filter(user=user)
    pending_request_qs = friend_request_qs.filter(status='pending')
    friend_request_form = FriendRequestForm(request.POST)
    context = {
        'object_qs':pending_request_qs,
        'form': friend_request_form,
    }
    if friend_request_form.is_valid():
        request_status = friend_request_form.cleaned_data.get('request_status')
        friend_name  = friend_request_form.cleaned_data.get('name')
        friend = friend_request.objects.filter(user=friend_name)
        print(friend)



    return render(request, 'userprofile/my_friend_requests.html', context)


def my_friends(request):
    user = request.user
    friend_request_qs = friend_request.objects.filter(user = user)
    accepted_request_qs = friend_request_qs.filter(status='accepted')



    print(accepted_request_qs)
    context = {
        'object_qs' : accepted_request_qs ,
    }
    return render(request,'userprofile/my_friends.html', context)






class ProfileDetailSlugView(DetailView):

    queryset = Userprofile.objects.all()
    template_name = "userprofile/profile.html"





    def get_context_data(self, *args, **kwargs):

        context = super(ProfileDetailSlugView, self).get_context_data(*args, **kwargs)
        return context




    def get_object(self, *args, **kwargs):
        request = self.request
        print(request)
        slug = self.kwargs.get('slug')

                # instance = get_object_or_404(Product, slug=slug, active=True)
        try:
            instance = Userprofile.objects.get(slug=slug)
        except Userprofile.DoesNotExist:
            raise Http404("Not found..")
        except Userprofile.MultipleObjectsReturned:
            qs = Userprofile.objects.filter(slug=slug)
            instance = qs.first()
        except:
            raise Http404("Uhhmmm ")
        return instance