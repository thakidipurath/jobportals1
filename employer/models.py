from django.db import models
from users.models import User

# Create your models here.
class EmployerProfile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,null=True)
    company_name = models.CharField(max_length=50)
    description = models.CharField(max_length=150)
    address = models.CharField(max_length=150)

    def __str__(self):
        return self.user

class Jobs(models.Model):
    company_name=models.ForeignKey(EmployerProfile,on_delete=models.CASCADE,null=True)
    post=models.CharField(max_length=50)
    experience=models.CharField(max_length=50)
    skill = models.CharField(max_length=120)
    description=models.CharField(max_length=150)
    posted_date=models.DateField(auto_now_add=True, null=True)
    last_date=models.DateField()