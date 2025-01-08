from django import forms
from django.contrib.auth.models import User

class RegistrationForm(forms.Form):
    username = forms.CharField(max_length=150, required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}), required=True)
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}), required=True)
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm Password'}), required=True)

    # def clean(self):
    #     cleaned_data = super().clean()
    #     password1 = cleaned_data.get('password1')
    #     password2 = cleaned_data.get('password2')

    #     if password1 and password2 and password1 != password2:
    #         raise forms.ValidationError("Passwords do not match.")
    #     return cleaned_data


