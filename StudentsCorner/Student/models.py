from django.db import models

# Create your models here.

from Teacher.models import User

class Student(models.Model):
    CHOICE = [
        ('cse','Computer Engineering'),
        ('eee','Eletrical Engineering'),
        ('civil','Civil Engineering'),
        ('mech','Mechanical Engineering'),
        ('ice','Instrumental Engineering'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50,null=False,blank=False)
    email = models.EmailField(unique=True,null=False,blank=False)
    roll_no = models.PositiveIntegerField(null=False,blank=False,unique=False)
    parrent_phno = models.PositiveIntegerField(null=False,blank=False) 
    whatsno = models.IntegerField(blank=False,null=False)
    department = models.CharField(max_length=5,choices=CHOICE,null=False,blank=False,default='cse')

    def __str__(self):
        return self.user.username

    class Meta():
        ordering = ["roll_no"]
    
