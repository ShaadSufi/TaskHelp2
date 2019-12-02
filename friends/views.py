from django.shortcuts import render
from .models import Friends


# Create your views here.

def friends_home(request):
    user_ = request.user
    user = Friends.objects.filter(user = user_).first()
    #my friends
    friends_lst = user.friends.all()

    # friend_requests
    user = Friends.objects.filter(user=user_).first()
    friend__request_lst = user.friend_requests.all()
    #



    context = {
        'friends_lst' : friends_lst,
        'friend__request_lst'  : friend__request_lst,
    }

    return render(request,'friends/home.html', context)

