from django.db import models
from accounts.models import User





class Friends(models.Model):
    user = models.ForeignKey(User, null=True, blank=True, related_name='user')
    friends =  models.ManyToManyField(User, blank=True, related_name='user_friends')
    friend_requests =  models.ManyToManyField(User, blank=True, related_name='friend_requests')

    def __str__(self):
        return self.user.full_name