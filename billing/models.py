from django.conf import settings
from django.db import models
from django.db.models.signals import post_save

User = settings.AUTH_USER_MODEL

class BillingProfile(models.Model):
    user = models.OneToOneField(User, null=True, blank=True)
    email = models.EmailField()
    active = models.BooleanField(default=True)
    update = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email

# def billing_profile_created_reciever(sender, instance, created, *args, **kwargs):
#     if created :
#         print("send to stripe/braintree")
#         instance.customer_id = newID
#         instance.save()

def user_created_reciever(sender, instance, created, *args, **kwargs):
    if created:
        BillingProfile.objects.get_or_create(user=instance, email = instance.email)

post_save.connect(user_created_reciever, sender= User)
