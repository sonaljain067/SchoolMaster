from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import *

urlpatterns = [
    path('token/',TokenObtainPairView.as_view()),
    path('token/refresh', TokenRefreshView.as_view()),

    path('school/list', AdminSchoolListView.as_view()),
    path('school-student/list',AdminSchoolStudentListView.as_view()),
    path('grade/create', AdminGradeCreateView.as_view()),

    path('school/create',SchoolCreateView.as_view(),name='create_school'),
    # path('school/create',create_school,name='create_school'),
    path('school/student/create', SchoolStudentCreateView.as_view()),
    path('school/student/list',SchoolStudentListView.as_view()),

    path('student/update/<int:id>', StudentUpdateView.as_view())
]