from decimal import Decimal
from django.conf import settings
from django.db import models
from django.db.models.signals import pre_save, post_save, m2m_changed
from accounts.models import User
from products.models import Product


User = settings.AUTH_USER_MODEL
REQUESTS_STATUS_CHOICES = (
    ('accepted','accepted'),
    ('rejected','Recieved'),
    ('pending','Pending'),
    ('on its way','on its way'),
    ('delivered', 'delivered'),
    )
FRIEND_REQUESTS_STATUS_CHOICES = (
    ('accepted','accepted'),
    ('rejected','rejected'),
    ('pending','pending'),
    )

class RequestsManager(models.Manager):
    def new_or_get(self, request):
        requests_id = request.session.get("cart_id", None)
        qs = self.get_queryset().filter(id=requests_id)
        if qs.count() == 1:
            new_obj = False
            requests_obj = qs.first()
            if request.user.is_authenticated() and requests_obj.user is None:
                requests_obj.user = request.user
                requests_obj.save()
        else:
            requests_obj = Requests.objects.new(user=request.user)
            new_obj = True
            request.session['requests_id'] = requests_obj.id
        return requests_obj, new_obj

    def new(self, user=None):
        user_obj = None
        if user is not None:
            if user.is_authenticated():
                user_obj = user
        return self.model.objects.create(user=user_obj)

    def create_request(self,user ,product, status):
        return Requests.objects.create(user = user, product= product, status=status)

    def get_by_user(self, user):
        user_id = user.id
        qs = self.get_queryset().filter(user=user_id)
        return qs

    def create_friend_request(self, user,reciever):
        return friend_request.objects.create(user=user,reciever=reciever)

    def get_past_requests(self, user: User, offset: int = 0, limit: int = 10):
        requests = Requests.objects.filter(user=user).order_by('-product__timestamp')[offset:limit+offset]
        return requests



class Requests(models.Model):
    user = models.ForeignKey(User, null=True, blank=True)
    product = models.ForeignKey(Product,  null=True, blank=True)
    status = models.CharField(max_length=120, default='pending', choices=REQUESTS_STATUS_CHOICES)
    #product_owner = models.ForeignKey(User, null=True, blank=True , related_name='userp')


    objects = RequestsManager()

    def __str__(self):
        return str(self.product)

class friend_request(models.Model):
    user = models.ForeignKey(User, null=True, blank=True)
    reciever = models.ForeignKey(User,null=True,blank=True, related_name="friend_request_reciever")
    status = models.CharField(max_length=120, default='pending', choices=FRIEND_REQUESTS_STATUS_CHOICES)

    objects = RequestsManager()

    def __str__(self):
        return str(self.user)





def pre_save_owner_update(sender, instance, *args, **kwargs):
    product_name = instance.product
    title = Product.objects.get_by_title(product_name)
    product_owner = Product.objects.get_userp_by_title(title)
    instance. product_owner =  product_owner

pre_save.connect(pre_save_owner_update, sender=Requests)