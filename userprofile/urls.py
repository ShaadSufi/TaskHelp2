from django.conf.urls import url

from .views import (

        my_profile,
        my_tasks,
        task_requests,
        #ProfileDetailSlugView,
        friend_requests,
        my_friends,
        profile_detail,
        friend_profile_about,
        friend_profile_friends,
        friend_profile_task_history,
        friend_profile_task,

)

urlpatterns = [
    url(r'^$',my_profile , name='my_profile'),
    url(r'^my_tasks/$',my_tasks , name='my_tasks'),
    url(r'^task_requests/$',task_requests , name='task_requests'),
    url(r'^(?P<slug>[\w-]+)/$',profile_detail, name = 'profile_detail'),
    url(r'^friend_request/$',friend_requests , name='friend_requests'),
    url(r'^my_friends/$',my_friends , name='my_friends'),
    url(r'^(?P<slug>[\w-]+)/about/$',friend_profile_about, name = 'friend_profile_about'),
    url(r'^(?P<slug>[\w-]+)/tasks/$',friend_profile_task, name = 'friend_profile_task'),
    url(r'^(?P<slug>[\w-]+)/task_history/$',friend_profile_task_history, name = 'friend_profile_task_history'),
    url(r'^(?P<slug>[\w-]+)/friends/$',friend_profile_friends, name = 'friend_profile_friends'),



]
