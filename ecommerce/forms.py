from django import forms
from django.contrib.auth import get_user_model
# from requests.models import Requests

User = get_user_model()

class ContactForm(forms.Form):
    fullname = forms.CharField(
        widget = forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder" : "Your full name"

            }
        )
    )
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "class": "form-control",
                "placeholder": "Your email"

            }
        )
    )
    content = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "class": "form-control",
                "placeholder": "Your message"

            }
        )
    )

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if not "bilkent.edu.tr" in email:
            raise forms.ValidationError("Email must be registered from Bilkent University")
        return email




# class RequestsForm(forms.ModelForm):
#     class Meta:
#         model = Requests
#         fields = ('title', 'publication_date', 'author', 'price', 'pages', 'book_type', )

