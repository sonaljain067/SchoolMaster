from rest_framework import permissions
from .models import *

class IsAdmin(permissions.BasePermission):
    def has_permission(self,request,view):
        return request.user.is_authenticated and request.user.role == 'Admin'
    
class IsSchool(permissions.BasePermission):
    def has_permission(self,request,view):
        return request.user.is_authenticated and request.user.role == 'school'
    
class IsStudent(permissions.BasePermission):
    def has_permission(self,request,view):
        return request.user.is_authenticated and (request.user.role == 'student' or request.user.role == 'school')
    