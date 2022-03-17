from django.shortcuts import render
from rest_framework.views import APIView
from employer.models import EmployerProfile,Jobs
from employer.serializers import EmployerSerializer,JobSerializer,UsercreationSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics, mixins, viewsets
from users.models import User


# Create your views here.

class EmployerRegisterView(viewsets.ViewSet):
    model = EmployerProfile
    serializers = EmployerSerializer

    def list(self, request):
        employer = EmployerProfile.objects.all()
        serializer = EmployerSerializer(employer, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = EmployerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class UserCreationView(generics.GenericAPIView,
#                        mixins.CreateModelMixin):
#     serializer_class = UsercreationSerializer
#     queryset = User.objects.all()
#     model = User
#
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)

class JobView(viewsets.ViewSet):
    model = Jobs
    serializers = JobSerializer

    def create(self, request):
        serializer = JobSerializer()
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def list(self, request):
        job = Jobs.objects.all()
        serializer = JobSerializer(job, many=True)
        return Response(serializer.data)




