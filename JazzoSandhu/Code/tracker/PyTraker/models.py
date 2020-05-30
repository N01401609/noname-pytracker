from django.db import models

# Create your models here
import datetime
from django.utils import timezone

class Comments(models.Model):
    comments = models.CharField(max_length=255)
    username = models.CharField(max_length=50)

    def __str__(self):
            return self.comments + ' - ' + self.username