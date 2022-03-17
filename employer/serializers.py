from rest_framework.serializers import ModelSerializer
from employer.models import EmployerProfile,Jobs
from django.contrib.auth.models import User, AbstractUser

class EmployerSerializer(ModelSerializer):
    class Meta:
        model = EmployerProfile
        fields =['user','company_name','description','address']
        read_only_fields = ['id', 'user']

class UsercreationSerializer(ModelSerializer):
    class Meta:
        model = User
        fields =['username','password','email']
    # def create(self, validated_data):
    #     return User.objects.create_user(**validated_data)

class  JobSerializer(ModelSerializer):
    class Meta:
        model = Jobs
        fields=['company_name','post','experience','skill','description','posted_date','last_date']