import os
import random
from django.db import models
from accounts.models import User
from requests.models import Requests
from products.models import Product
from django.conf import settings
#User = settings.AUTH_USER_MODEL
from ecommerce.utils import unique_slug_generator_for_user
from django.db.models.signals import pre_save
from django.core.urlresolvers import reverse




def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext

def upload_image_path(instance, filename):
    # print(instance)
    #print(filename)
    new_filename = random.randint(1,3910209312)
    name, ext = get_filename_ext(filename)
    final_filename = '{new_filename}{ext}'.format(new_filename=new_filename, ext=ext)
    return "products/{new_filename}/{final_filename}".format(
            new_filename=new_filename,
            final_filename=final_filename
            )


class Userprofile(models.Model):
    user = models.ForeignKey(User, null=True, blank=True)
    email =  models.CharField(max_length=120,  null=True, blank=True)
    full_name = models.CharField(max_length=120,  null=True, blank=True)
    image = models.ImageField(upload_to=upload_image_path, null=True, blank=True)
    phone = models.CharField(max_length=12)
    products =  models.ManyToManyField(Product, blank=True)
    slug = models.SlugField(blank=True, unique=True)
    friends = models.ManyToManyField(User, blank=True, related_name='friends')



    #recieved_requests = models.ManyToManyField(Requests, blank=True)
    #sent_requests = models.ManyToManyField(Requests, blank=True)


    def __str__(self):
        return self.user.get_full_name()

    def get_absolute_url(self):
        return reverse('userprofile', kwargs={'slug': self.slug})

def full_name_pre_save_reciever(sender, instance, *args, **kwargs):
    user= instance.user
    instance.full_name = user.full_name

def email_pre_save_reciever(sender, instance, *args, **kwargs):
    user= instance.user
    instance.email = user.email


def profile_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator_for_user(instance)

pre_save.connect(full_name_pre_save_reciever, sender=Userprofile )
pre_save.connect(profile_pre_save_receiver, sender=Userprofile)
pre_save.connect(email_pre_save_reciever, sender=Userprofile )



class Profile(models.Model):
    user= models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default = 'default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user}Profile'







# def upload_product_file_loc(instance, filename):
#     slug = instance.product.slug
#     #id_ = 0
#     id_ = instance.id
#     if id_ is None:
#         Klass = instance.__class__
#         qs = Klass.objects.all().order_by('-pk')
#         if qs.exists():
#             id_ = qs.first().id + 1
#         else:
#             id_ = 0
#     if not slug:
#         slug = unique_slug_generator(instance.product)
#     location = "product/{slug}/{id}/".format(slug=slug, id=id_)
#     return location + filename #"path/to/filename.mp4"



