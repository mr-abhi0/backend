from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from .models import Students


class StudentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Students
        fields = ['id', 'stuname', 'email']
