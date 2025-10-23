# todo/forms.py
from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'done']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Task title', 'class': 'form-control'}),
            'description': forms.Textarea(attrs={'rows':3, 'class': 'form-control'}),
            'done': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
