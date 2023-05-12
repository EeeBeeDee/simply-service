from allauth.account.forms import SignupForm
from django import forms


class CustomSignupForm(SignupForm):
    phone = forms.IntegerField(label='Phone Number:')


    def signup(self, request, user):
        user.phone = self.cleaned_data['phone']
        user.save()
        return user
