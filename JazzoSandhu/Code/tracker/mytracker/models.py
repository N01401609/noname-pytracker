from django.db import models

# Create your models here.
import datetime
from django.utils import timezone

class Users(models.Model):
    userID = models.CharField(max_length=50)

class Comments(models.Model):
    comment_text = models.CharField(max_length=255)
    posted_date = models.DateTimeField('posted date')

