from django.shortcuts import render
from .serializers import StudentsSerializer
from .models import Students
from rest_framework.generics import ListAPIView
# Create your views here.


class StudentsList(ListAPIView):
    queryset = Students.objects.all()
    serializer_class = StudentsSerializer
