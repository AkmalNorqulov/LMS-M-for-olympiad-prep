from django.contrib import admin
from .models import Homework

@admin.register(Homework)
class HomeworkAdmin(admin.ModelAdmin):
    list_display = ('title', 'due_time', 'created_at')
    search_fields = ('title', 'description')
    list_filter = ('created_at',)
