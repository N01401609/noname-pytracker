from django.contrib import admin

# Register your models here.
# register your models class here for managing it threw admin panel
from .models import Comments
admin.site.register(Comments)
