from django.contrib import admin
from .models import * 

admin.site.register(CustomUser)
admin.site.register(SchoolInfo)
admin.site.register(StudentInfo)
admin.site.register(Grade)