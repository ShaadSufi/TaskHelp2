from django.conf.urls import url

from .views import (

    requests_home,
    friend_request,
    PastRequests

)

urlpatterns = [

    url(r'^$', requests_home, name='home'),
    url(r'^friend_request/$', friend_request, name='friend_request'),
    url(r'^past_request/$', PastRequests.as_view(), name='past_requests'),
    url(r'^past_request_cancel/(?P<id>\d+)/$', PastRequests.as_view(), name='past_request_cancel'),
]