from django.db import models
from django.contrib.auth.models import User

class Job(models.Model):
    title = models.CharField(max_length=225,blank=True,null=True)
    task_id = models.CharField(max_length=225,blank=True,null=True)
    customer = models.CharField(max_length=225,blank=True,null=True)
    territory = models.CharField(max_length=225,blank=True,null=True)
    status = models.CharField(max_length=225,blank=True,null=True)
    vacancies = models.CharField(max_length=225,blank=True,null=True)
    qualification_type = models.CharField(max_length=225,blank=True,null=True)
    specialization = models.CharField(max_length=225,blank=True,null=True)
    category = models.CharField(max_length=225,blank=True,null=True)
    min_exp = models.FloatField(blank=True,null=True)
    max_exp = models.FloatField(blank=True,null=True)
    gulf_exp = models.FloatField(blank=True,null=True)
    salary_type = models.CharField(max_length=225,blank=True,null=True)
    currency = models.FloatField(blank=True,null=True)
    from_amount = models.FloatField(blank=True,null=True)
    to_amount = models.FloatField(blank=True,null=True)
    amount = models.FloatField(blank=True,null=True)
    description = models.TextField(blank=True, null=True)
    working_hours = models.CharField(max_length=225,blank=True,null=True)
    transportation = models.CharField(max_length=225,blank=True,null=True)
    contract_period_yr = models.IntegerField(blank=True,null=True)
    contract_period_mn = models.IntegerField(blank=True,null=True)
    joining_ticket = models.CharField(max_length=225,blank=True,null=True)
    food = models.CharField(max_length=225,blank=True,null=True)
    accommodation = models.CharField(max_length=225,blank=True,null=True)
    leave = models.CharField(max_length=225,blank=True,null=True)
    visa_type = models.CharField(max_length=225,blank=True,null=True)
    nationality = models.CharField(max_length=225,blank=True,null=True)
    overtime = models.CharField(max_length=225,blank=True,null=True)
    any_other_allowance = models.CharField(max_length=225,blank=True,null=True)

    created_by = models.ForeignKey(User, related_name='jobs', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    changed_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Userprofile(models.Model):
    user = models.OneToOneField(User, related_name='userprofile',on_delete=models.CASCADE)
    is_employer =  models.BooleanField(default = False)
    username = models.CharField(max_length=225,blank=True)
    fullname = models.CharField(max_length=225,blank=True,null=True)
    gender = models.CharField(max_length=225,blank=True,null=True)
    marital_status = models.CharField(max_length=225,blank=True,null=True)
    mobile = models.IntegerField(blank=True,null=True)
    email = models.EmailField(max_length=225,blank=True,null=True)
    alternate_email = models.EmailField(max_length=225,blank=True,null=True)
    skype_id = models.CharField(max_length=225,blank=True,null=True)
    alternate_contact = models.IntegerField(blank=True,null=True)
    imo_number = models.IntegerField(blank=True,null=True)
    address = models.CharField(max_length=225,blank=True,null=True)
    address = models.CharField(max_length=225,blank=True,null=True)
    district = models.CharField(max_length=225,blank=True,null=True)
    state = models.CharField(max_length=225,blank=True,null=True)
    pincode = models.IntegerField(blank=True,null=True)
    
    # territory = models.CharField(max_length=225,blank=True,null=True)
    # status = models.CharField(max_length=225,blank=True,null=True)
    # vacancies = models.CharField(max_length=225,blank=True,null=True)
    # qualification_type = models.CharField(max_length=225,blank=True,null=True)
    # specialization = models.CharField(max_length=225,blank=True,null=True)
    # category = models.CharField(max_length=225,blank=True,null=True)

User.userprofile = property(lambda u:Userprofile.objects.get_or_create(user=u)[0])

class Application(models.Model):
    job = models.ForeignKey(Job, related_name='applications', on_delete=models.CASCADE)
    task_id = models.CharField(max_length=225,blank=True,null=True)
    description = models.TextField(null=True)
    # userprofile = models.ForeignKey(Userprofile,related_name='applications', on_delete=models.CASCADE)

    created_by = models.ForeignKey(User, related_name='applications', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)