from rest_framework import generics  
from rest_framework.views import APIView
from django.contrib.auth.hashers import make_password
from rest_framework.response import Response 
from  rest_framework import status 
from rest_framework.renderers import JSONRenderer
from .models import *
from .serializers import *
from .permissions import *
    
# class UpdateEmail(APIView):
#     def post(request):
#         email = request.data['email']
#         school = SchoolInfo.objects.
# Admin View
class AdminSchoolListView(generics.ListAPIView):
    permission_classes = [IsAdmin]
    serializer_class = SchoolSerializer
    queryset = SchoolInfo.objects.all()

class AdminSchoolStudentListView(generics.ListAPIView):
    permission_classes = [IsAdmin]
    serializer_class = StudentSerializer

    def get_queryset(self):
        school_id = self.request.query_params.get('school', None)
        grade = self.request.query_params.get('grade', None)
        queryset = StudentInfo.objects.all()
        if school_id is not None: 
            queryset = queryset.filter(school__id = school_id)
        if grade is not None: 
            queryset = queryset.filter(grade = grade)
        return queryset
    
class AdminGradeCreateView(generics.CreateAPIView):
    permission_classes = [IsAdmin]
    queryset = Grade.objects.all()
    serializer_class = GradeSerialier


# School View
class SchoolCreateView(generics.CreateAPIView):
    serializer_class = SchoolSerializer
    queryset = SchoolInfo.objects.all()


class SchoolStudentCreateView(APIView):
    def post(self, request):
        student = StudentInfo.objects.create(
            school = SchoolInfo.objects.get(id=request.data['school']),
            grade = Grade.objects.get(grade = request.data['grade']),
            name = request.data['name'],
            username =  request.data['username'], 
            password = make_password(request.data['password']),
            email = request.data['email']
        )
        serializer = StudentSerializer(student)
        if serializer.data:
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SchoolStudentListView(generics.ListAPIView):
    permission_classes = [IsSchool]
    serializer_class = StudentSerializer

    def get_queryset(self):
        user = self.request.user.email
        school = SchoolInfo.objects.filter(email = user).first()

        grade = self.request.query_params.get('grade', None)
        queryset = StudentInfo.objects.all().filter(school = school)

        if grade is not None: 
            queryset = queryset.filter(grade = grade)
        return queryset 
    
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    

# student view
class StudentUpdateView(generics.UpdateAPIView):
    permission_classes = [IsSchool, IsStudent]
    queryset = StudentInfo.objects.all()
    lookup_field = 'id'
    serializer_class = StudentSerializer