from django.core.management.base import BaseCommand
from employeeinfo.models import User,JobDetails
from datetime import datetime, timedelta
import random
from faker import Faker
from django.utils import timezone
#instance for the Faker object
fakedata = Faker()
from random import randint

class Command(BaseCommand):
    help = 'Fake Users Creation'

    ''' Run this command to create users (python manage.py users_creation 5 )'''

    def add_arguments(self, parser):
        parser.add_argument('no_of_users', type=int)

    def handle(self, *args, **kwargs):
        no_of_users = kwargs['no_of_users']
        for fakeuser in range(no_of_users):
          fake_id = fakedata.bothify(text='??#?##?##').upper()
          fake_name = fakedata.name()
          fake_tz = fakedata.timezone()
          role = fakedata.job()
          location = fakedata.address()
          total_exp = fakedata.random_int(0, 10)
          skills = fakedata.job()
          job_desc = fakedata.sentence()
          image_url = fakedata.image_url()
          # Create new user Entry
          user = User.objects.create(id=fake_id,name=fake_name,tz=fake_tz)
          acty = JobDetails.objects.create(user=user,role=role,location=location,total_exp=total_exp,skills=skills,job_desc=job_desc,image_url=image_url)
       
        return str(no_of_users)+' Users Created Succesfully'