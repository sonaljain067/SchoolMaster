from rest_framework import serializers
from .models import *

class GradeSerialier(serializers.ModelSerializer):
    class Meta:
        model = Grade
        fields = ['grade']

class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = SchoolInfo
        fields = '__all__'

class StudentSerializer(serializers.ModelSerializer):
    school_name = serializers.CharField(source='school.name', read_only=True)
    grade = serializers.CharField(source='grade.grade',read_only=True)

    class Meta:
        model = StudentInfo
        fields = ['school_name','name','username','grade','email']


