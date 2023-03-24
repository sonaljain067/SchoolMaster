from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class CustomUserManager(BaseUserManager):
    def create_user(self,email,password=None,**extra_fields):
        if not email:
            raise ValueError("Email is required!!")

        email = self.normalize_email(email)
        user = self.model(email=email,**extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user 
    
    def create_superuser(self,email,password=None,**extra_fields):
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_superuser', True)
        
        user = self.create_user(email,password,role="Admin",**extra_fields)
        return user 

class CustomUser(AbstractBaseUser):
    ADMIN = 'admin'
    SCHOOL = 'school'
    STUDENT = 'student'
    ROLE_CHOICES = [
        (ADMIN, 'Admin'),
        (SCHOOL, 'School'),
        (STUDENT, 'Student')
    ]
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=20,choices=ROLE_CHOICES,default="")
    is_active = models.BooleanField(default=True)
    is_staff=models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = CustomUserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def has_perm(self, perm):
        return True 
    
    def has_module_perms(self,user_obj):
        return True 
    
    def __str__(self):
        return self.email 

class Grade(models.Model):
    grade = models.CharField(max_length=250)

class SchoolInfo(models.Model):
    name = models.CharField(max_length=250)
    email = models.CharField(max_length=250)
    city = models.CharField(max_length=250)
    pin_code = models.CharField(max_length=250)
    password = models.CharField(max_length=250)

class StudentInfo(models.Model):
    school = models.ForeignKey(SchoolInfo,on_delete=models.CASCADE)
    email = models.CharField(max_length=250)
    name = models.CharField(max_length=250)
    username = models.CharField(max_length=250)
    password = models.CharField(max_length=250)
    grade = models.ForeignKey(Grade, on_delete=models.CASCADE)