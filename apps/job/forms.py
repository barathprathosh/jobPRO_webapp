from django import forms

from .models import Job, Application, Userprofile

class UserprofileForm(forms.ModelForm):
    class Meta:
        model = Userprofile
        fields = ['user','firstname','lastname']

class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ['job','description','task_id','created_by']
