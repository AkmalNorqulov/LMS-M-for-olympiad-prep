from django import forms
from .models import Lesson, Task


class LessonForm(forms.ModelForm):
    class Meta:
        model = Lesson
        fields = ['day', 'title', 'start_time', 'end_time', 'description']


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['day', 'title', 'description', 'due_time', 'completed']
