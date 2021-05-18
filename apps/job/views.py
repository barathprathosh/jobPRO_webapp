from django.shortcuts import render,redirect, HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Job
from .forms import ApplicationForm
import logging
logger = logging.getLogger(__name__)

@login_required
def job_detail(request,job_id):
    job = Job.objects.get(pk=job_id)
    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        if form.is_valid():
            application = form.save(commit=False)
            application.job = job
            application.task_id = job.task_id
            application.description = "test"
            application.created_by = request.user
            application.save()
            return redirect('dashboard')
    else:
        form = ApplicationForm()
    return render(request, 'job/job_detail.html', {'job':job})

# def search(request):
#     return render(request,'job/search.html')

def apply_for_job(request,job_id):
    test = Job.objects.get(pk="108")
    return render(request, 'core.html')


@login_required
def dashboard(request):
    return render(request, 'job/dashboard.html',{'userprofile':request.user.userprofile})

def handleRefer(request):
    if request.method=="POST":
        # Get the post parameters
        jobid=request.POST['jobid']
        fullname=request.POST['fullname']
        email=request.POST['email']
        mobile=request.POST['mobile']

        # if len(mobile)>=10:
        #     messages.error(request, " Your Mobile No. must be 10 digits")
        #     return redirect('frontpage')

        # refer to friends
        if request.method == 'POST':
            form = ApplicationForm(request.POST)
        if form.is_valid():
            refer = form.save(commit=False)
            # refer.jobid = jobid
            refer.fullname = fullname
            refer.mobile = mobile
            refer.email = email
            refer.created_by = request.user
            refer.save()
        return redirect('frontpage')

    return HttpResponse("404- Not found")