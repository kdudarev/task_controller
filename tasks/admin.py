from django.contrib import admin

from tasks.models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('name', 'text', 'date_added', 'deadline',
                    'reporter', 'assignee', 'status', 'priority')
    list_display_links = ('name', 'text')
    search_fields = ('name', 'text', 'deadline', 'status')
