from django.contrib import admin

# Register your models here.
from .models import Friends


class ProductAdmin(admin.ModelAdmin):
    list_display = {'__str__' , 'slug'}
    class Meta :
        model = Friends




admin.site.register(Friends)
