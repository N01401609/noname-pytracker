from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from .models import Profile,Comments


class UserForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']


class ProfileForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = Profile
        fields = ['firstname', 'lastname', 'phonenumber', 'email']


class CommentForm(forms.ModelForm):
    comment = forms.CharField(required=True, widget=forms.Textarea)
    class Meta:
        model = Comments
        fields = [
            'user',
            'comment',
            'comment_date'
        ]

    def clean_title(self):
        user = self.cleaned_data.get("user")

class CommentRawProduction(forms.Form):
    user = forms.CharField()
    comment = forms.CharField(required=True, widget=forms.Textarea)
    comment_date = forms.DateTimeField()

