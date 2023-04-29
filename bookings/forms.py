from django import forms
from .models import Bookings
from django.forms import  TextInput, DateInput, NumberInput, TimeInput, EmailInput

class BookingsForm(forms.ModelForm):
    class Meta:
        model = Bookings
        fields = ['restaurant', 'time', 'date', 'no_of_adults', 'no_of_children', 'name', 'email', 'number']
        widgets = {
            'restaurant': TextInput(attrs={
                'class': 'form-control',
            }),
            'time': TimeInput(attrs={
                'class': 'form-control',
            }),
            'date': DateInput(attrs={
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
                'min': '1',
                'max': '9',
                'placeholder': 'no of children',
            }),
            'email': EmailInput(attrs={
                'class': 'form-control',
            }),
            'number': NumberInput(attrs={
                'class': 'form-control',
            }),
        }
