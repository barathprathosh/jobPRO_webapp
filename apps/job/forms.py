from django import forms

from .models import Job, Application

# class AddJobForm(forms.ModelForm):
#     class Meta:
#         model = Job
#         fields = ['title','short_discription','long_discription']

class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ['description']