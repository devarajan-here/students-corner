from django.urls import path

from . import views

app_name = 'student'

urlpatterns = [
    path('signup/',views.StudentRegister,name='signup'),
    path('detail/<int:pk>',views.StudetDetail.as_view(),name='detail'),
]