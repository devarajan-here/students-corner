from django.urls import path,include
from . import views
from django.contrib.auth import views as auth_views

app_name = 'teacher'

urlpatterns = [
    path('',views.TeacherRegister,name='signup'),
    path('detail/<int:pk>',views.TeacherDetail.as_view(),name='detail'),
    path('update/<int:pk>',views.TeacherUpdateView,name='update'),
    # nxt 
    # teacher/group/creategroup (create-form)
    # teacher/group/editgroup (update-form)
    # teacher/group/<grpname>/attendance (mark attendance)
    # teacher/group/<grpname>/Edit-attendance (Edit attendance)
    # path('<slug:username>/',views.TeacherDetail.as_view(),name='TeacherDetail')
]