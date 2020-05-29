from django.db import models

# Create your models here.
from django.db import models


# Does not need primary key is automatically created

# INVOICES TABLE
class Invoice(models.Model):
    # Will not use foreign key until other models are created
    user_id = models.IntegerField()
    project_id = models.IntegerField()
    date_created = models.DateTimeField('date created')
    due_date = models.DateTimeField('due date')


# CLIENTS TABLE
class Client(models.Model):
    client_name = models.CharField(max_length=200)
    client_email = models.CharField(max_length=200)
    client_address = models.CharField(max_length=200)
    client_phone = models.CharField(max_length=200)

