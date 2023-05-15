from datetime import date
from django import forms
from django.forms import (DateInput, NumberInput,
                          TimeInput, EmailInput, Select)
from django.contrib.auth.models import User
from user_profiles.models import UserProfile
from .models import Bookings


class BookingsForm(forms.ModelForm):
    """
    Form used in bookings.html template. Connects to Bookings model
    """


    class Meta():
        model = Bookings
        fields = ['restaurant', 'time', 'date', 'no_of_adults',
                  'no_of_children', 'email', 'number']
        widgets = {
            'restaurant': Select(attrs={
                'class': 'form-control',
                'value': '1',
            }),
            'time': TimeInput(attrs={
                'type': 'time',
                'class': 'form-control',
            }),
            'date': DateInput(attrs={
                'type': 'date',
                'min': date.today().strftime('%Y-%m-%d'),
                'class': 'form-control',
            }),
            'no_of_adults': NumberInput(attrs={
                'class': 'form-control',
                'min': '1',
                'max': '9',
                'placeholder': 'no of adults',
            }),
            'no_of_children': NumberInput(attrs={
                'class': 'form-control',
                'min': '0',
                'max': '9',
                'placeholder': 'no of children',
            }),
            'email': EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your Email',
            }),
            'number': NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your Phone Number',
            }),
        }

