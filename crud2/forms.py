# from django.forms import ModelForm
from .models import Person

from django import forms
# from django.core import validators


class studentregister(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['first_name','last_name','email','password']

        widgets = {
        'first_name':forms.TextInput(attrs={'class':'form-control'}),
        'last_name':forms.TextInput(attrs={'class':'form-control'}),
        'email':forms.EmailInput(attrs={'class':'form-control'}),
        'password':forms.PasswordInput(render_value=True, attrs={'class':'form-control'}),
        }