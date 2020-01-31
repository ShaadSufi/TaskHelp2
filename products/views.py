
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.views.generic import ListView, DetailView, View
from django.shortcuts import render, get_object_or_404, redirect
from carts.models import Cart
from .models import Product
from .forms import AddProductForm
from django.contrib import messages
from django.views.generic import RedirectView
from comments.models import Comment
from django.contrib.contenttypes.models import ContentType
from accounts.models import User
from django.views.generic.edit import FormMixin
from django import forms
from django.http import HttpResponseForbidden
from django.core.urlresolvers import reverse, reverse_lazy



class ProductFeaturedListView(ListView):
    template_name = "products/list.html"

    def get_queryset(self, *args, **kwargs):
        request = self.request
        return Product.objects.all().featured()


class ProductFeaturedDetailView(DetailView):
    queryset = Product.objects.all().featured()
    template_name = "products/featured-detail.html"

    # def get_queryset(self, *args, **kwargs):
    #     request = self.request
    #     return Product.objects.featured()


class ProductListView(ListView):
    template_name = "products/list.html"

    # def get_context_data(self, *args, **kwargs):
    #     context = super(ProductListView, self).get_context_data(*args, **kwargs)
    #     print(context)
    #     return context

    def get_context_data(self, *args, **kwargs):
        context = super(ProductListView, self).get_context_data(*args, **kwargs)
        cart_obj, new_obj = Cart.objects.new_or_get(self.request)
        context['cart'] = cart_obj
        return context

    def get_queryset(self, *args, **kwargs):
        request = self.request
        return Product.objects.all()

class ProductLikeToggle(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        slug = self.kwargs.get('slug')
        obj = get_object_or_404(Product, slug=slug)
        url_ = obj.get_absolute_url()
        user = self.request.user
        if user.is_authenticated():
            if user in obj.likes.all():
                obj.likes.remove(user)
            else:
                obj.likes.add(user)
        return url_


def product_list_view(request):
    queryset = Product.objects.all()
    context = {
        'object_list': queryset
    }
    return render(request, "products/list.html", context)


class ProductDetailSlugView(DetailView):


    queryset = Product.objects.all()
    template_name = "products/detail.html"




    def get_context_data(self, *args, **kwargs):

        context = super(ProductDetailSlugView, self).get_context_data(*args, **kwargs)
        product_userp_list = User.objects.all()
        userp = product_userp_list[0].full_name
        cart_obj, new_obj = Cart.objects.new_or_get(self.request)
        context['cart'] = cart_obj
        context['userp'] = userp
        return context




    def get_object(self, *args, **kwargs):
        request = self.request


        slug = self.kwargs.get('slug')

                # instance = get_object_or_404(Product, slug=slug, active=True)
        try:
            instance = Product.objects.get(slug=slug, active=True)
        except Product.DoesNotExist:
            raise Http404("Not found..")
        except Product.MultipleObjectsReturned:
            qs = Product.objects.filter(slug=slug, active=True)
            instance = qs.first()
            view_lst = []
            view_lst.append(request.user)
            instance.views = view_lst
        except:
            raise Http404("Uhhmmm ")
        return instance






def product_detail_view(request, pk=None, *args, **kwargs):
    # instance = Product.objects.get(pk=pk, featured=True) #id
    # instance = get_object_or_404(Product, pk=pk, featured=True)
    # try:
    #     instance = Product.objects.get(id=pk)
    # except Product.DoesNotExist:
    #     print('no product here')
    #     raise Http404("Product doesn't exist")
    # except:
    #     print("huh?")

    instance = Product.objects.get_by_id(pk)
    if instance is None:
        raise Http404("Product doesn't exist")
    # print(instance)
    # qs  = Product.objects.filter(id=pk)

    # #print(qs)
    # if qs.exists() and qs.count() == 1: # len(qs)
    #     instance = qs.first()
    # else:
    #     raise Http404("Product doesn't exist")

    context = {
        'object': instance
    }
    return render(request, "products/detail.html", context)

def add_product(request):
    add_product_form = AddProductForm(request.POST)

    context = {
        'page_title' : "Add Product",
        'form' : add_product_form,

    }
    if add_product_form.is_valid():
        print(add_product_form)
        title = add_product_form.cleaned_data.get('product_title')
        description = add_product_form.cleaned_data.get('product_description')
        destination = add_product_form.cleaned_data.get('destination')
        tip = add_product_form.cleaned_data.get('tip')
        # image = add_product_form.cleaned_data.get('image')
        new_product = Product.objects.create_product(title, description, destination, tip)
        messages.success(request, "Product created successfully")
        print(new_product)
        print("Product creation successful")
    return render(request, 'products/add_product.html', context)

# def add_comment_view(request):
#     add_comment_form = AddCommentForm(request.POST)
#     context = {
#
#         'form' : add_comment_form
#     }
#     if add_comment_form.is_valid():
#         comment_user = request.user
#         comment_text = add_comment_form.cleaned_data.get('comment_text')
#         new_comment = Comment.objects.create(comment_user, comment_text)
#         messages.success(request, "Comment added successfully")
#         print(new_comment)


    #     print("Product creation successful")
    # return render(request, 'products/detail.html', context)


# class TaskForm(forms.Form):
#     CHOICES=[('accept','accept'),
#              ('reject','reject')]
#
#     task_status = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)
#
#
# class ProductDetailSlugView(FormMixin, DetailView):
#     model = Product
#     form_class = TaskForm
#     template_name = "products/detail.html"
#
#     def get_success_url(self):
#         if kwargs != None:
#             return reverse_lazy('products/')
#
#
#     def get_context_data(self, **kwargs):
#         context = super(ProductDetailSlugView, self).get_context_data(**kwargs)
#         context['form'] = self.get_form()
#         return context
#
#     def post(self, request, *args, **kwargs):
#         if not request.user.is_authenticated():
#             return HttpResponseForbidden()
#         self.object = self.get_object()
#         form = self.get_form()
#         if form.is_valid():
#             return self.form_valid(form)
#         else:
#             return self.form_invalid(form)
#
#     def form_valid(self, form):
#         # Here, we would record the user's interest using the message
#         # passed in form.cleaned_data['message']
#         return super(ProductDetailSlugView, self).form_valid(form)
#         def form_valid(self, form):
#             # Here, we would record the user's interest using the message
#             # passed in form.cleaned_data['message']
#             return super(ProductDetailSlugView, self).form_valid(form)