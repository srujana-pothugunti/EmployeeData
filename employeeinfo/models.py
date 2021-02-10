from django.db import models

# Create your models here.
class User(models.Model):
    id = models.CharField(max_length=10, primary_key=True)
    name = models.CharField(max_length = 70)
    tz = models.CharField(max_length = 80)

    def __str__(self):
        return self.name

class JobDetails(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    role = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    total_exp = models.IntegerField(default=0)
    skills = models.CharField(max_length=200)
    job_desc = models.CharField(max_length=200)
    image_url = models.CharField(max_length=100)

    def __str__(self):
        return self.user.name