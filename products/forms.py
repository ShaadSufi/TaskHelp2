from django import forms
from django.contrib.auth import get_user_model



User = get_user_model()



class AddProductForm(forms.Form):

    product_title = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Product title"

            }
        )
    )
    product_description = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Describe specifics your product"

            }
        )
    )
    destination = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Where can this task be done/ product be found :"

            }
        )
    )
    tip = forms.DecimalField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "How much are you offering to complete this task : "

            }
        )
    )
    # image = forms.ImageField()



class TaskForm(forms.Form):
    CHOICES=[('accept','accept'),
             ('reject','reject')]

    task_status = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)
