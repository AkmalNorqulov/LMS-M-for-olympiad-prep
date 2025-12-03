from django import forms
from .models import Homework

class HomeworkForm(forms.ModelForm):
    class Meta:
        model = Homework
        fields = ['title', 'description', 'due_time']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Homework title'}),
            'description': forms.Textarea(attrs={'placeholder': 'Description', 'rows': 4}),
            'due_time': forms.TextInput(attrs={'placeholder': 'e.g., 2024-12-10 or 10:30 AM'}),
        }