from django import forms
from django.contrib.auth import get_user_model



User = get_user_model()





class FriendRequestForm(forms.Form):
    CHOICES=[('accepted','accept'),
             ('rejected','reject')]

    request_status = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)

    #
    # user = models.ForeignKey(User, null=True, blank=True)
    # full_name = models.CharField(max_length=120,  null=True, blank=True)
    # image = models.ImageField(upload_to=upload_image_path, null=True, blank=True)
    # phone = models.CharField(max_length=

class EditProfileForm(forms.Form):

    full_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Name"

            }
        )
    )
    phone = forms.DecimalField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Phone #"

            }
        )
    )

    # image = forms.ImageField()