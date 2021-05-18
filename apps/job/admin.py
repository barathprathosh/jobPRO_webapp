from django.contrib import admin

from .models import Job,Application,Userprofile,Refer

admin.site.register(Job)
admin.site.register(Application)
admin.site.register(Userprofile)
admin.site.register(Refer)