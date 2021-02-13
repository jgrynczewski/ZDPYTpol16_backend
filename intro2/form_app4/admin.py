from django.contrib import admin

from form_app4.models import Task

# Register your models here.
# admin.site.register(Task)

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
