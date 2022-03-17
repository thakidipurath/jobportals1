from django.db import models
from django.contrib.auth.models import User, AbstractUser

# Create your models here.

class User(AbstractUser):
     options=(("employer","employer"),
              ("candidate","candidate"),
     )
     role=models.CharField(max_length=12,choices=options,default="candidate")



