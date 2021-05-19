from django.contrib import admin

from .models import Job,Application,Userprofile

admin.site.register(Job)
admin.site.register(Application)
admin.site.register(Userprofile)