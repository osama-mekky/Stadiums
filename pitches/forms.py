from .models import *
from django import forms
from django.forms import ModelForm

class DateInput(forms.DateInput):
    input_type = 'date'

class RestaurantForm(forms.ModelForm):

    class Meta:
        model = OpeningHours

        fields = ('made_on','period', 'from_hour', 'to_hour','timing',)
        widgets = {
            'made_on': DateInput(attrs={'class':'form-control'}),
            'period':forms.Select(attrs={'class':'form-control'}),
            'from_hour':forms.TextInput(attrs={'class':'form-control'}),
            'to_hour':forms.TextInput(attrs={'class':'form-control'}),
            'timing':forms.Select(attrs={'class':'form-control'}),
        }