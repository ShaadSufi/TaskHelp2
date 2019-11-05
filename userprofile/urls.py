from django.conf.urls import url

from .views import (

        my_profile,
        my_tasks,
        task_requests,
        ProfileDetailSlugView,
        friend_requests,
        my_friends,
)

urlpatterns = [
    url(r'^$',my_profile , name='my_profile'),
    url(r'^my_tasks/$',my_tasks , name='my_tasks'),
    url(r'^task_requests/$',task_requests , name='task_requests'),
    url(r'^(?P<slug>[\w-]+)/$',ProfileDetailSlugView.as_view(), name = 'profile_view'),
    url(r'^friend_request/$',friend_requests , name='friend_requests'),
    url(r'^my_friends/$',my_friends , name='my_friends'),


]
