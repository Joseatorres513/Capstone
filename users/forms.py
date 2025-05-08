from django import forms
from django.contrib.auth.forms import User
from .models import Profile

class SignupForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'password']

class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['picture', 'phone_number', 'street', 'city', 'state', 'zip_code']
