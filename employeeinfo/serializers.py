from django.shortcuts import render
from rest_framework.serializers import ModelSerializer, SerializerMethodField
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.views.decorators.http import require_POST, require_GET
from django.http import HttpResponse, JsonResponse
from employeeinfo.models import *


# Create your views here.


class UserSerializer(ModelSerializer):
    job_info = SerializerMethodField()

    class Meta:
        model = User
        depth = 1
        fields = ('id', 'name', 'tz','job_info')

    def get_job_info(self, user):
        context = []
        job_details = user.jobdetails_set.all()
        for job in job_details:
            data = {}
            data['role'] = job.role
            data['location'] = job.location
            data['total_exp'] = job.total_exp
            data['skills'] = job.skills
            data['job_desc'] = job.job_desc
            data['image_url'] = job.image_url
            context.append(data)

        return context


@require_GET
@csrf_exempt
def users(request):
    '''
        url = 'http://127.0.0.1:8000/api/users/'
    '''

    # try:
    users = User.objects.all()
    status = True
    response = UserSerializer(users, many=True).data

    # except ValidationError:
    #     status = False
    #     data = ["Something went wrong"]

    return JsonResponse({
        'ok': status,
        'members': response
    })