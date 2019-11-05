from django.conf.urls import url

from .views import (
        sentrequest,


        )

urlpatterns = [
    url(r'^sent/$', sentrequest, name='sentrequest'),
    ]