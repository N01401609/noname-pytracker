from django.contrib.auth.models import User
from django.db import models

# Create your models here.
import datetime
from django.utils import timezone


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    firstname = models.CharField(verbose_name="first name", max_length=50)
    lastname = models.CharField(verbose_name="last name", max_length=50)
    phonenumber = models.CharField(verbose_name="phone number", max_length=10)
    email = models.CharField(verbose_name="email", max_length=100)


class WorkDiary(models.Model):
    userID = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    date = models.DateTimeField()
    projectID = models.ForeignKey(Projects, on_delete=models.CASCADE)
    projectNotesID = models.ForeignKey(ProjectNotes, on_delete=models.CASCADE)
    taskID = models.ForeignKey(Tasks, on_delete=models.CASCADE)
    taskNotesID = models.ForeignKey(TaskNotes, on_delete=models.CASCADE)