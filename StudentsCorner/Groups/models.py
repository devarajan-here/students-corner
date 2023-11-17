from django.db import models
from django.shortcuts import reverse
# Create your models here.

from Teacher.models import User
from django.utils.text import slugify
from Student.models import Student 

class Group(models.Model):
    classes = [
        ('cse','Computer Engineering'),
        ('eee','Eletrical Engineering'),
        ('civil','Civil Engineering'),
        ('mech','Mechanical Engineering'),
        ('ice','Instrumental Engineering'),
    ]

    name = models.CharField(max_length=40,blank=False,null=False)
    slug = models.SlugField(allow_unicode=True,unique=True)
    for_class = models.CharField(max_length=5,null=False,choices=classes,default='cse',blank=False)
    class_start_date = models.DateField(null=False,blank=False)
    students = models.ManyToManyField(User,through='GroupMembers')

    def __str__(self):
        return self.name

    def save(self,*args,**kwargs):
        self.slug = slugify(self.name)
        super().save(*args,**kwargs)

    def get_absolute_url(self):
        return reverse('groups:group_list',kwargs={'slug':self.name})


class GroupMembers(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE,related_name='membership')
    students = models.ForeignKey(User, on_delete=models.CASCADE,related_name='user_groups')
    join_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.user.username

    class Meta():
        unique_together = ('group','students')

class Attendence(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    students = models.ManyToManyField(Student,through="AttendanceStatus")
    date = models.DateField(auto_now_add=False)

    def __str__(self):
        return f"Attendance for {self.group.name} on {self.date}"

class AttendanceStatus(models.Model):
    attendance = models.ForeignKey(Attendence,on_delete=models.CASCADE)
    student = models.ForeignKey(Student,on_delete=models.CASCADE)
    is_present = models.BooleanField()

    def __str__(self):
        return f"{self.student.name} {self.attendance.group.name} {self.attendance.date}"


    # is_present = models.BooleanField(default=False)
    # absent_student = models.ManyToManyField(Student, on_delete=models.CASCADE, related_name='absent attendance')
    # present_student = models.ManyToManyField(Student, on_delete=models.CASCADE, related_name='present_attendance')