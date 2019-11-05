from django import forms
#from django.contrib.auth import get_user_model
from datetime import date
#User = get_user_model()



class RequestsForm(forms.Form) :



    from_date = forms.DateField(
        label='Enter date of borrow :',
        widget=forms.SelectDateWidget
    )

    till_date = forms.DateField(
        label='Enter date of return : ',
        widget=forms.SelectDateWidget
    )


    # def clean_date_limit(self):
    #     from_date = self.cleaned_data.get("from_date")
    #     till_date = self.cleaned_data.get("till_date")
    #     delta = till_date - from_date
    #     if delta.days >= 3:
            #raise forms.ValidationError("Passwords must match")
    #    return data

    # def clean(self):
    #     data  = self.cleaned_data
    #     password = self.cleaned_data.get("password")
    #     password2 = self.cleaned_data.get("password2")
    #     if password != password2:
    #         raise forms.ValidationError("Passwords must match")
    #     return data
    #
    # def clean_email(self):
    #     email = self.cleaned_data.get("email")
    #     if not "bilkent.edu.tr" in email:
    #         raise forms.ValidationError("Email must be registered from Bilkent University")
    #     return email
