from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    firstname = models.CharField(verbose_name="first name", max_length=50)
    lastname = models.CharField(verbose_name="last name", max_length=50)
    phonenumber = models.CharField(verbose_name="phone number", max_length=10)
    email = models.CharField(verbose_name="email", max_length=100)


