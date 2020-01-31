import random
import os
from django.db import models
from django.db.models.signals import pre_save
from ecommerce.utils import unique_slug_generator
from django.core.urlresolvers import reverse
from django.db.models import Q
from django.conf import settings
from accounts.models import User





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

class ProductQuerySet(models.query.QuerySet):
    def active(self):
        return self.filter(active=True)

    def featured(self):
        return self.filter(featured=True, active=True)

    def search(self, query):
        lookups = (Q(title__icontains=query) |
                  Q(description__icontains=query) |
                  Q(price__icontains=query) |
                  Q(tag__title__icontains=query)
                  )
        # tshirt, t-shirt, t shirt, red, green, blue,
        return self.filter(lookups).distinct()

    def get_userp_by_title(self, title):
        qs = self.get_queryset().filter(title=title)  # Product.objects == self.get_queryset()
        product = qs.first()
        userp_qs = product.userp
        userp = userp_qs.first()
        return userp


class ProductManager(models.Manager):
    def get_queryset(self):
        return ProductQuerySet(self.model, using=self._db)

    def all(self):
        return self.get_queryset().active()


    def featured(self): #Product.objects.featured()
        return self.get_queryset().featured()

    def get_by_id(self, id):
        qs = self.get_queryset().filter(id=id) # Product.objects == self.get_queryset()
        if qs.count() == 1:
            return qs.first()
        return None

    def search(self, query):
        return self.get_queryset().active().search(query)

    def create_product(self,title, description, destination, tip):
        return Product.objects.create(title=title, description=description, destination= destination, tip=tip)

    def get_by_userp(self, userp):
        user_id = userp.id
        qs = self.get_queryset().filter(userp = user_id)
        return qs
        #first find the id of the userp
        #userp = userp.id
        #userp_qs = []
        #userp_qs.append(userp)
        #qs = self.get_queryset().filter(userp = userp_qs) # Product.objects == self.get_queryset()
        #return type(qs)

    def get_by_title(self,title):
        qs = self.get_queryset().filter(title = title) # Product.objects == self.get_queryset()
        product = qs.first()
        return product

    def get_userp_by_title(self,title):
        qs = self.get_queryset().filter(title = title) # Product.objects == self.get_queryset()
        product = qs.first()
        userp_qs = product.userp
        userp = userp_qs.first()
        return userp

    def get_liked_products_by_user(self, user):
        like_product_qs = []
        #user_id = user.id
        all_product_qs = Product.objects.all()
        for product in all_product_qs:
            like_user_qs = product.likes.all()
            if user in like_user_qs :
                like_product_qs.append(product)
        return like_product_qs
        


class Product(models.Model):
    userp           = models.ManyToManyField(User, blank=True, related_name='product_owner')
    title           = models.CharField(max_length=120)
    slug            = models.SlugField(blank=True, unique=True)
    description     = models.TextField()
    price           = models.DecimalField(decimal_places=2, max_digits=20, default=0.00)
    image           = models.ImageField(upload_to=upload_image_path, null=True, blank=True)
    likes           = models.ManyToManyField(User, blank=True, related_name='post_likes')
    featured        = models.BooleanField(default=False)
    active          = models.BooleanField(default=True)
    timestamp       = models.DateTimeField(auto_now_add=True)
    is_digital      = models.BooleanField(default=False) # User Library
    destination     = models.CharField(max_length=120, null=True, blank=True)
    tip             = models.DecimalField(default=0.00, max_digits=100, decimal_places=2)
    views           = models.ManyToManyField(User, blank=True, related_name='product_viewers')
    objects = ProductManager()

    def get_absolute_url(self):
        #return "/products/{slug}/".format(slug=self.slug)
        return reverse("products:detail", kwargs={"slug": self.slug})

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title

    @property
    def name(self):
        return self.title


    def get_downloads(self):
        qs = self.productfile_set.all()
        return qs

    def get_like_url(self):
        return reverse("products:like-toggle", kwargs={'slug': self.slug})

    # def userp(self):
    #     return self.owner


# def product_pre_save_user(sender, instance, *args, **kwargs):
#     instance.user = User


def product_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

pre_save.connect(product_pre_save_receiver, sender=Product)
#pre_save.connect(product_pre_save_user, sender=Product)


def upload_product_file_loc(instance, filename):
    slug = instance.product.slug
    #id_ = 0
    id_ = instance.id
    if id_ is None:
        Klass = instance.__class__
        qs = Klass.objects.all().order_by('-pk')
        if qs.exists():
            id_ = qs.first().id + 1
        else:
            id_ = 0
    if not slug:
        slug = unique_slug_generator(instance.product)
    location = "product/{slug}/{id}/".format(slug=slug, id=id_)
    return location + filename #"path/to/filename.mp4"



