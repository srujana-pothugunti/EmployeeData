from django.shortcuts import render
from django.http import Http404
from .models import User,JobDetails


def index(request):
    employee_list = JobDetails.objects.all()
    context = []
    for emp in employee_list:
        data = {}
        data['user_name'] = emp.user.name
        data['tz'] = emp.user.tz
        data['role'] = emp.role
        data['location'] = emp.location
        data['total_exp'] = emp.total_exp
        data['skills'] = emp.skills
        data['job_desc'] = emp.job_desc
        data['image_url'] = emp.image_url
        context.append(data)
    return render(request, 'index.html', {'employee_data':context})
