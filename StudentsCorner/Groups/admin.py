from django.contrib import admin

# Register your models here.

from . import models


class GroupMembersInline(admin.TabularInline):
    model = models.GroupMembers

admin.site.register(models.Group)
admin.site.register(models.Attendence)
admin.site.register(models.AttendanceStatus)