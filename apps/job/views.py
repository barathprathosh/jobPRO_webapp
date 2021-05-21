from django.shortcuts import render,redirect, HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Job
from .forms import ApplicationForm
import logging
import requests
import json
from django.utils.html import format_html
logger = logging.getLogger(__name__)


def job_detail(request,job_id):
    job = Job.objects.get(pk=job_id)
    if request.method == 'POST':
        # form = ApplicationForm(request.POST)
        # if form.is_valid():
            # application = form.save(commit=False)
            # application.job = job.title
            # application.task_id = job.task_id
            # application.description = "test"
            # application.created_by = request.user
            # application.save()
        application_create = "https://myjobpro.teamproit.com/api/resource/Application"
        requestHeaders = {
                'Content-Type': 'application/x-www-form-urlencoded',
                'Accept': 'application/json',
                'Authorization': 'token 7070d9b1afcdbe0:38d8e57acf7f19f'
            }
        data = json.dumps({"candidate_name":"TEST"})
        response = requests.request("POST",application_create,headers=requestHeaders,data = data)
        return redirect('dashboard')
        # else:
        #     form = ApplicationForm()
    return render(request, 'job/job_detail.html', {'job':job})

# def search(request):
#     return render(request,'job/search.html')

@login_required
def userprofile(request):
    return render(request, 'job/dashboard.html',{'userprofile':request.user.userprofile})

@login_required
def dashboard(request):
    return render(request, 'job/dashboard.html',{'userprofile':request.user.userprofile})

def handleRefer(request):
    if request.method=="POST":
        # Get the post parameters
        jobid=request.POST['jobid']
        fullname=request.POST['fullname']
        email_id=request.POST['email']
        mobile=request.POST['mobile']

        # Sent API refer
        refer_mail = "https://myjobpro.teamproit.com/api/method/myjobpro.api.send_email"
        requestHeaders = {
                'Content-Type': 'application/x-www-form-urlencoded',
                'Accept': 'application/json',
                'Authorization': 'token 7070d9b1afcdbe0:38d8e57acf7f19f'
            }
        data = json.dumps({
            "jobid":jobid,
            "fullname":fullname,
            "email_id":email_id,
            "mobile":mobile
            })
        response = requests.request("GET",refer_mail,headers=requestHeaders,data = data)
        messages.success(request," Mail sent successfully ")
        return redirect('frontpage')

    else:
        return HttpResponse("404 - Not found")
