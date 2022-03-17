from django.shortcuts import render
from candidate.models import Candiate_profile
from candidate.serializers import CandidateSerializer
from employer.serializers import JobSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics, mixins, viewsets
from users.models import User
from employer.models import Jobs
from rest_framework.decorators import action


# Create your views here.

class CandidateViewSet(viewsets.ModelViewSet):
    model = Candiate_profile
    queryset = Candiate_profile.objects.filter()
    serializer_class = CandidateSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def list(self, request):
        todo = Jobs.objects.all()
        serializer = JobSerializer(todo, many=True)
        return Response(serializer.data)

    #     api/v1/portal/candidate/matching_jobs
    @action(methods=["GET"], detail=False)
    def matching_jobs(self, request, *args, **kwargs):
        jobs = Jobs.objects.filter(skills__contains=request.user.candidate.skills)
        serializer = JobSerializer(jobs, many=True)
        return Response(serializer.data)
