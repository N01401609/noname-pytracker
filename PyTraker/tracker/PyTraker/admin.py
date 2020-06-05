from django.contrib import admin

# Register your models here.

from .models import Profile, Projects, Clients, Invoices, Tasks, Comments

from .models import Profile, Projects, Clients, Invoices, Tasks, Timers, TaskNotes, ProjectNotes

admin.site.register(Profile)

admin.site.register(Projects)

admin.site.register(Clients)

admin.site.register(Invoices)

admin.site.register(Tasks)

admin.site.register(Comments)


admin.site.register(Timers)

admin.site.register(TaskNotes)

admin.site.register(ProjectNotes)

