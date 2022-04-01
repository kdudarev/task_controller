from django.contrib import admin

from tasks.models import Task, Profile


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('name', 'text', 'date_added', 'deadline',
                    'reporter', 'assignee', 'status', 'priority')
    list_display_links = ('name', 'text')
    search_fields = ('name', 'text', 'deadline', 'status')


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user',)
    list_display_links = ('user',)
    search_fields = ('user',)
