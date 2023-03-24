from django.db.models.signals import post_save
from django.dispatch import receiver 
from .models import * 

@receiver(post_save, sender = SchoolInfo)
def create_schoolinfo(sender,instance,created,**kwargs):
    if created:
        user = CustomUser.objects.create(email=instance.email,role='school')
        user.set_password(instance.password)
        user.save()

@receiver(post_save, sender = StudentInfo)
def create_studentinfo(sender,instance,created,**kwargs):
    if created:
        user = CustomUser.objects.create(email=instance.email,role='student')
        user.set_password(instance.password)
        user.save()