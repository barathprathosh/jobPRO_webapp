from apps.job.models import Job

import requests
import json

def my_cron_job():
    print("**********success*************8")
    task_url = "https://v13.teamproit.com/api/resource/Task?fields=[%22name%22,%22subject%22,%22service%22,%22territory%22,%22description%22,%22customer%22,%22project%22,%22currency%22,%22amount%22,%22amount%22,%22job_category%22,%22creation%22,%22minimum_experience%22,%22maximum_experience%22,%22qualification%22,%22specialization%22,%22salary_type%22,%22from%22,%22to%22]&&filters=[[%22service%22,%22==%22,%22REC-I%22],[%22service%22,%22==%22,%22REC-D%22],[%22status%22,%22!=%22,%22Completed%22],[%22status%22,%22!=%22,%22Cancelled%22],[%22status%22,%22!=%22,%22Hold%22]]&&limit_page_length=5000"
    response = requests.request("GET", task_url)
    byte_str = response.content
    dict_str = byte_str.decode("UTF-8")
    job_response = json.loads(dict_str)
    for j in job_response["data"]:
        a = Job(title =j["name"],short_description = j["subject"], long_description = j["territory"],created_by = request.user)
        a.save()