from django import forms
from . import models

class ProjectCreateForm(forms.ModelForm):
    class Meta:
        model=models.Project
        fields=['title','description']
        widgets={
            'title':forms.TextInput(),
            'description':forms.Textarea()
        }


class ProjectUpdateForm(forms.ModelForm):
    class Meta:
        model=models.Project
        fields=['title', 'status']
        widgets={
            'title':forms.TextInput(),
            'status':forms.Select(),
        }