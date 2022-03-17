from django.db import models
from django.contrib.auth.models import User
from users.models import User
# Create your models here.
class Candiate_profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    candidate_name = models.CharField(max_length=100)
    qualification = models.CharField(max_length=50)
    cv = models.ImageField(upload_to="images")
    skills = models.CharField(max_length=200)
    experience = models.CharField(max_length=200)