from django.shortcuts import render,redirect
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
    return render(request, 'cor.html')


@login_required
def dashboard(request):
    return render(request, 'job/dashboard.html',{'userprofile':request.user.userprofile})