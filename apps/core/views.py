from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage
from django.contrib import messages
# from blog.models import Post
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
        jobs_url = "https://myjobpro.teamproit.com/api/resource/Position?fields=[%22job_description%22,%22work_hrs%22,%22contract_period_year%22,%22food%22,%22accommodation%22,%22transportation%22,%22salary_range%22,%22about_client%22,%22name%22,%22specialization%22,%22subject%22,%22status%22,%22country%22,%22min_exp%22,%22max_exp%22,%22salary_currency%22,%22salary_range%22,%22qualification%22]&&filters=[[%22status%22,%22=%22,%22Active%22],[%22web%22,%22=%22,%220%22]]&&limit_page_length=5000"
        response = requests.request("GET", jobs_url)
        byte_str = response.content
        dict_str = byte_str.decode("UTF-8")
        job_response = json.loads(dict_str)
        for j in job_response["data"]:
            a = Job(title =j["subject"],specialization = j["specialization"],salary_type = j["salary_range"],description = j["job_description"],working_hours = j["work_hrs"],contract_period_yr = j["contract_period_year"],food = j["food"],accommodation = j["accommodation"],transportation = j["transportation"],customer = j["about_client"],qualification_type = j["qualification"],task_id = j["name"],territory = j["country"],status = j["status"],min_exp = j["min_exp"],max_exp = j["max_exp"],created_by = request.user)
            a.save()
            job_created = "https://myjobpro.teamproit.com/api/resource/Position/%s"%j["name"]
            requestHeaders = {
                    'Content-Type': 'application/x-www-form-urlencoded',
                    'Accept': 'application/json'
                }
            data = json.dumps({"web":"1"})
            response = requests.request("PUT",job_created,headers=requestHeaders,data = data)
    return render(request, 'core/frontpage.html',{'jobs': page})

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

def handleSignUp(request):
    if request.method=="POST":
        # Get the post parameters
        username=request.POST['username']
        email=request.POST['email']
        fname=request.POST['fname']
        lname=request.POST['lname']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']

        # check for errorneous input
        # if len(username)<10:
        #     messages.error(request, " Your user name must be under 10 characters")
        #     return redirect('frontpage')

        # if not username.isalnum():
        #     messages.error(request, " User name should only contain letters and numbers")
        #     return redirect('frontpage')
        if (pass1!= pass2):
             messages.error(request, " Passwords do not match")
             return redirect('frontpage')
        
        # Create the user
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name= fname
        myuser.last_name= lname
        myuser.save()
        user_created = "https://myjobpro.teamproit.com/api/resource/User"
        requestHeaders = {
                'Content-Type': 'application/x-www-form-urlencoded',
                'Accept': 'application/json'
            }
        data = json.dumps({
            "email":email,
            "first_name":fname,
            "last_name":lname,
            "new_password":pass1
            })
        response = requests.request("POST",user_created,headers=requestHeaders,data = data)
        messages.success(request, " Your Job Portal has been successfully created")
        return redirect('frontpage')

    else:
        return HttpResponse("404 - Not found")


def handeLogin(request):
    if request.method=="POST":
        # Get the post parameters
        loginusername=request.POST['loginusername']
        loginpassword=request.POST['loginpassword']

        user=authenticate(username= loginusername, password= loginpassword)
        if user is not None:
            login(request, user)
            messages.success(request, "Successfully Logged In")
            return redirect("frontpage")
        else:
            messages.error(request, "Invalid credentials! Please try again")
            return redirect("frontpage")

    return HttpResponse("404- Not found")

    return HttpResponse("login")

def handelLogout(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect('frontpage')
