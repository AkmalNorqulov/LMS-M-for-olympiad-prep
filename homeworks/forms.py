from django import forms
from .models import Homework

class HomeworkForm(forms.ModelForm):
    class Meta:
        model = Homework
        fields = ['title', 'description', 'due_date', 'due_time']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Homework title', 'class': 'form-control'}),
            'description': forms.Textarea(attrs={'placeholder': 'Description', 'rows': 4, 'class': 'form-control'}),
            'due_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'due_time': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}),
        }