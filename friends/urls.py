from django.conf.urls import url

from .views import (

    friends_home,
)

urlpatterns = [
    url(r'^$',friends_home , name='friends_home'),
    # url(r'^my_tasks/$',my_tasks , name='my_tasks'),
    # url(r'^task_requests/$',task_requests , name='task_requests'),
    # url(r'^(?P<slug>[\w-]+)/$',ProfileDetailSlugView.as_view(), name = 'profile_view'),
    # url(r'^friend_request/$',friend_requests , name='friend_requests'),
    # url(r'^my_friends/$',my_friends , name='my_friends'),


]
