"""Admin configuration for the tasks app."""
from django.contrib import admin

from .models import Task


class TaskAdmin(admin.ModelAdmin):
    """Admin interface for the Task model."""

    list_display = ('title', 'description', 'completed')


admin.site.register(Task, TaskAdmin)
