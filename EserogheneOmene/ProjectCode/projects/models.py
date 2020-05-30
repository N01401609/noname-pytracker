from django.db import models

# Create your models here.
#
# What makes up a project
# Project Name
# Company the project is for(client)
# Project Start Date
# Project Due Date
# Project Description

from django.db import models

class Project(models.Model):
    name = models.CharField(max_length=200)
    client = models.CharField(max_length=200)
    start_date = models.DateTimeField('start date')
    due_date = models.DateTimeField('due date')
    description = models.CharField(max_length=1000)
    def __str__(self):
        return self.name



