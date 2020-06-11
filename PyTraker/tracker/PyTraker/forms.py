from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from .models import Profile, Comments, Projects

# for import date and time
from _datetime import datetime
from django.utils import timezone
from django.template import defaultfilters


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
            'comment_date',
        ]


    def clean_title(self):
        user = self.cleaned_data.get("user")



class CommentRawProduction(forms.Form):
    user = forms.CharField()
    comment = forms.CharField(required=True, widget=forms.Textarea)
    comment_date = forms.DateTimeField()


class ProjectForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(ProjectForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs = {'class': 'form-control', }
        self.fields['description'].widget.attrs = {'class': 'form-control', }
        self.fields['clientID'].widget.attrs = {'class': 'form-control', }
        self.fields['payRate'].widget.attrs = {'class': 'form-control', }
        self.fields['startDate'].widget.attrs = {'class': 'form-control', }
        self.fields['dueDate'].widget.attrs = {'class': 'form-control', }

        # for visible in self.visible_fields():
        #     visible.field.widget.attrs['class'] = 'form-control'
    class Meta:
        model = Projects
        fields = ['name', 'description', 'clientID', 'payRate', 'startDate', 'dueDate']
        labels = {'name': 'Name', 'description': 'Description', 'clientID': 'Client', 'payRate': 'Pay Rate',
                  'startDate': 'Start Date', 'dueDate': 'Due Date'}
