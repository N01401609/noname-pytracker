from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from .models import Profile, WorkDiary


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


class WorkDiaryForm(forms.ModelForm):
    name = forms.CharField()
    date = forms.DateTimeField()

    class Meta:
        model = WorkDiary
        fields = ['userID', 'name', 'date', 'projectID', 'projectNotesID', 'taskID', 'taskNotesID']

        # def clean_user(self, *args, **kwargs):
        #   userID = self.cleaned_data.get("userID")
