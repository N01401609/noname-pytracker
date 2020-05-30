from django.contrib import admin

from .models import User, Note

# admin.site.register(User)
# admin.site.register(Note)
admin.site.site_header = "Note Admin"

class NoteInline(admin.TabularInline):
    model = Note
    extra = 3


class UserAdmin(admin.ModelAdmin):
    fieldsets = [('First Name', {'fields': ['user_fname']}), ('Last Name', {'fields': ['user_lname']})]
    inlines = [NoteInline]


admin.site.register(User, UserAdmin)