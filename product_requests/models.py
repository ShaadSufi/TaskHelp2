from django.db import models
from django.conf import settings
from django.db import models
from django.db.models.signals import pre_save
from products.models import Product
# Create your models here.
#
#
User = settings.AUTH_USER_MODEL



class Product_Request(models.Model):
    sender        = models.ForeignKey(User, null=True, blank=True)
    product       = models.ForeignKey(Product, blank=True, null=True)
    reciever      = models.CharField(max_length=1200, blank=True, null=True)
    from_date     = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    till_date     = models.DateTimeField(null=True, blank=True)

    #product_owner = models.ForeignKey(Product.user, blank= True, null= True)

    def __str__(self):
        return str(self.product)

    # def clean_till_date(self):
    #     email = self.cleaned_data.get("email")
    #     if ((till_date - from_date) > 3):
    #         raise forms.ValidationError("This product cannot be shared for more than 3 days ")
    #     return email

def request_pre_save_receiver(sender, instance, *args, **kwargs):
    product_name = instance.product
    product = Product.objects.get_by_title(product_name)
    user = product.user
    instance.reciever = user


pre_save.connect(request_pre_save_receiver, sender=Product_Request)