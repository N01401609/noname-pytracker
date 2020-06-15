from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from .models import Profile, Comments, Projects, Invoices, Clients, WorkDiary

# for import date and time
from _datetime import datetime
from django.utils import timezone
from django.template import defaultfilters


class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class ProfileForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = Profile
        fields = ['firstname', 'lastname', 'phonenumber', 'email']

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class CommentForm(forms.ModelForm):
    comment = forms.CharField(required=True, widget=forms.Textarea)

    class Meta:
        model = Comments
        fields = [
            'user',
            'comment',
            'comment_date',
        ]

    def clean_user(self, *args, **kwargs):
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


class InvoiceForm(forms.ModelForm):
    class Meta:
        model = Invoices
        fields = ['userID',
                  'projectID',
                  'dateCreated',
                  'dueDate']


class WorkDiaryForm(forms.ModelForm):
    name = forms.CharField()
    date = forms.DateTimeField()

    class Meta:
        model = WorkDiary
        fields = ['userID', 'name', 'date', 'projectID', 'projectNotesID', 'taskID', 'taskNotesID']

        # def clean_user(self, *args, **kwargs):
        #   userID = self.cleaned_data.get("userID")
