from django.contrib import admin

from .models import Requests, friend_request

admin.site.register(Requests)
admin.site.register(friend_request)