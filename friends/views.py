from django.shortcuts import render
from .models import Friends
from userprofile.models import Userprofile




# Create your views here.

def friends_home(request):
    user_ = request.user
    user = Friends.objects.filter(user = user_).first()
    #my friends
    friends_lst = user.friends.all()
    friends_dict = {}
    for friend in friends_lst:
        print(friend)
        user  = Userprofile.objects.filter(email=friend).first()
        slug = user.slug
        friends_dict[friend] = slug




    # friend_requests
    user = Friends.objects.filter(user=user_).first()
    friend__request_lst = user.friend_requests.all()

    friend_request_dict = {}
    for friend in friend__request_lst:
        user = Userprofile.objects.filter(email=friend).first()
        slug = user.slug
        friend_request_dict[friend] = slug




    context = {
        'friends_lst' : friends_lst,
        'friends_dict': friends_dict,
        'friend__request_lst'  : friend__request_lst,
        'friend_request_dict': friend_request_dict,
    }

    return render(request,'friends/home.html', context)

def accept(request):
    user_ = request.user
    user = Friends.objects.filter(user=user_).first()
    friend__request_lst = user.friend_requests.all()

    context={}
    return render(request,'friends/home.html', context)

def reject(request):
    context={}
    return render(request,'friends/home.html', context)

