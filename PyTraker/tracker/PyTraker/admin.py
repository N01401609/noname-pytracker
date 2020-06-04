from django.contrib import admin

# Register your models here.

from .models import Profile,Projects,Clients,Invoices, Tasks
admin.site.register(Profile)

admin.site.register(Projects)

admin.site.register(Clients)

admin.site.register(Invoices)

admin.site.register(Tasks)