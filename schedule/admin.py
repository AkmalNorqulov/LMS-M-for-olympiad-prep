from django.contrib import admin
from .models import Lesson, Task


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('title', 'day', 'start_time', 'end_time')
    list_filter = ('day',)
    search_fields = ('title', 'description')


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'day', 'start_time', 'end_time')
    list_filter = ('day',)
    search_fields = ('title', 'description')
