"""ecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from .views import home_page,about_page,contact_page,my_orders
from accounts.views import login_page, register_page,logout_view, guest_register_view
from django.conf import settings
from django.conf.urls.static import static
#from django.contrib.auth.views import LogoutView
from products.views import add_product

#from comments.views import CommentLikeToggle
from products.views import  ProductListView





urlpatterns = [
    url(r'^$',  ProductListView.as_view(), name ='home'),
    url(r'^about/$', about_page, name ='about'),
    url(r'^contact/$', contact_page, name ='contact'),
    url(r'^orders/$',my_orders, name ='my_orders'),
    url(r'^login/$', login_page, name ='login'),
    url(r'^register/guest$', guest_register_view, name ='guest_register'),
    url(r'^logout/$',logout_view, name ='logout'),
    url(r'^register/$', register_page, name ='register'),
    url(r'^products/',include("products.urls" , namespace='products')),
    url(r'^product_requests/',include("product_requests.urls" , namespace='product_requests')),
    url(r'^search/', include("search.urls", namespace='search')),
    url(r'^accounts/', include("accounts.urls", namespace='accounts')),
    url(r'^cart/', include("carts.urls", namespace='cart')),
    url(r'^admin/', admin.site.urls),
    url(r'^add_product/$', add_product, name = 'add_product'),
    url(r'^requests/', include("requests.urls", namespace='requests')),
    url(r'^profile/', include("userprofile.urls", namespace='userprofile')),

]

if settings.DEBUG :
    urlpatterns = urlpatterns +  static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)