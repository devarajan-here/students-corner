from django.db import models
# from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser

# Create your models here.

# to custom user create model

class User(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)


class Teacher(models.Model):
    CHOICE = [
        ('cse','Computer Engineering'),
        ('eee','Eletrical Engineering'),
        ('civil','Civil Engineering'),
        ('mech','Mechanical Engineering'),
        ('ice','Instrumental Engineering'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(null=False,blank=False,unique=True)
    name = models.CharField(max_length=40, null=False,blank=False)
    whatsno = models.IntegerField(null=False,blank=False)
    department = models.CharField(max_length=20, choices=CHOICE,default='cse',blank=False)


    def __str__(self):
        return self.user.username
    
    def get_absolute_url(self):
        return reverse("teacher:detail",kwargs={"pk":self.pk})