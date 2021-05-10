from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.core.paginator import Paginator, EmptyPage

from apps.job.models import Job
# from apps.userprofile.models import Userprofile

import requests
import json


def frontpage(request):
    jobs = Job.objects.all()
    p = Paginator(jobs, 7)
    page_no = request.GET.get('page',1)
    try:
        page = p.page(page_no)
    except EmptyPage:
        page = p.page(1)
    # jobs_url = "https://myjobpro.teamproit.com/api/resource/Position?fields=[%22name%22,%22subject%22,%22status%22,%22country%22,%22min_exp%22,%22max_exp%22,%22salary_currency%22,%22salary_range%22,%22qualification%22]&&filters=[[%22status%22,%22=%22,%22Active%22],[%22web%22,%22=%22,%220%22]]&&limit_page_length=5000"
    # response = requests.request("GET", jobs_url)
    # byte_str = response.content
    # dict_str = byte_str.decode("UTF-8")
    # job_response = json.loads(dict_str)
    # for j in job_response["data"]:
    #     a = Job(title =j["subject"],task_id = j["name"],territory = j["country"], status = j["status"], min_exp = j["min_exp"], max_exp = j["max_exp"],created_by = request.user)
    #     a.save()
        # job_created = "https://myjobpro.teamproit.com/api/resource/Position/%s"%j["name"]
        # response = requests.request("PUT", job_created,body = {"web":1})
    return render(request, 'core/frontpage.html',{'jobs': page})

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()

            account_type = request.POST.get('account_type', 'jobseeker')
            username = request.POST.get('username')

            # if account_type == 'employer':
            #     userprofile = Userprofile.objects.create(user=user,username=username,is_employer=True)
            #     user.userprofile.save()
            # else:
            #     userprofile = Userprofile.objects.create(user=user,username=username)
            #     user.userprofile.save()

            login(request,user)

            return redirect('frontpage')
    else:
        form = UserCreationForm()

    return render(request, 'core/signup.html',{'form':form})

def search_result_view(request):
    """
        User can search job with multiple fields
    """

    job_list = Job.objects.all()

    # Keywords
    if 'job_title_or_company_name' in request.GET:
        job_title_or_company_name = request.GET['job_title_or_company_name']

        if job_title_or_company_name:
            job_list = job_list.filter(title__icontains=job_title_or_company_name) | job_list.filter(
                customer__icontains=job_title_or_company_name)

    # location
    if 'territory' in request.GET:
        territory = request.GET['territory']
        if territory:
            job_list = job_list.filter(territory__icontains=territory)

    context = {

        'page_obj': job_list,

    }
    # return render(request, 'job/result.html', context)
    return render(request, 'core/frontpage.html',{'jobs': job_list})
