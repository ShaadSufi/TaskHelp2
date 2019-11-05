from django.conf.urls import url

from .views import (

    requests_home,
    friend_request,

)

urlpatterns = [

    url(r'^$', requests_home, name='home'),
    url(r'^friend_request/$', friend_request, name='friend_request'),
]