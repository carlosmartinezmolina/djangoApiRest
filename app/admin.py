from django.contrib import admin

from . import models 

@admin.register(models.Task)
class Task(admin.ModelAdmin):
    list_display = ('task','taskId')
    search_fields = ('task','taskId')