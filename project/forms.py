from django import forms
from .models import projectFormat

class  AddNewProject(forms.ModelForm):

    class Meta:
        model = projectFormat
        fields =["title", "description", "tech_stack", "programmer", "image", "project_link"]