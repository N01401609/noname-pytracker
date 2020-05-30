from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from .models import Profile


class UserForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']


class ProfileForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = Profile
        fields = ['firstname', 'lastname', 'phonenumber', 'email']
