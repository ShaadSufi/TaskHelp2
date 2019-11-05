from django.shortcuts import render
from django.views.generic import RedirectView
from .models import Comment
from django.shortcuts import render, get_object_or_404, redirect
from .forms import AddCommentForm
from django.conf import settings
from django.contrib import messages

# Create your views here.
# class CommentLikeToggle(RedirectView):
#     def get_redirect_url(self, *args, **kwargs):
#         slug = self.kwargs.get('slug')
#         obj = get_object_or_404(Comment, slug=slug)
#         url_ = obj.get_absolute_url()
#         user = self.request.user
#         if user.is_authenticated():
#             if user in obj.likes.all():
#                 obj.likes.remove(user)
#             else:
#                 obj.likes.add(user)
#         return url_

#User = settings.AUTH_USER_MODEL
