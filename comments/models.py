from django.db import models
from django.conf import settings
from products.models import Product
#from django.contrib.contenttypes.fields import GenericForeignKey
#from django.contrib.contenttypes.models import ContentType
#from django.core.urlresolvers import reverse
#from ecommerce.utils import random_string_generator
#from django.db.models.signals import pre_save

User = settings.AUTH_USER_MODEL
class Comment(models.Model):
    user       = models.ForeignKey(User, null=True, blank=True)
    post       = models.ForeignKey(Product,  null=True, blank=True)
    timestamp  = models.DateTimeField(auto_now_add= True)
    content = models.TextField()
    #content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, null=True)
    #object_id = models.PositiveIntegerField(null=True)
    #content_object = GenericForeignKey('content_type', 'object_id')
    #likes = models.ManyToManyField(User, blank=True, related_name='comment_likes')
    #slug = models.SlugField(blank=True, unique=True)
    #likes

    def __str__(self):
        return str(self.user.username) + str(self.post)
#
#     def get_like_url(self):
#         return reverse("comments:like-toggle", kwargs={'slug': self.slug})
#
#     def get_absolute_url(self):
#         #return "/products/{slug}/".format(slug=self.slug)
#         return reverse("comments", kwargs={"slug": self.slug})
#
# def comment_pre_save_receiver(sender, instance, *args, **kwargs):
#     if not instance.slug:
#         instance.slug = random_string_generator(instance)
#
# pre_save.connect(comment_pre_save_receiver, sender=Comment)
#
#

