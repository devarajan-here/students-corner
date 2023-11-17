from django.urls import path

app_name = 'groups'

from . import views
urlpatterns = [
    path('create/',views.CreateGroup.as_view(),name='new'),
    path('<slug>/detail',views.GroupDetailView.as_view(),name='group_detail'),
    path('',views.GroupListView.as_view(),name='group_list'),
    path('join/<slug>/',views.GrpJoin.as_view(),name='group_join'),
    path('<slug>/leave',views.GrpLeave.as_view(),name='group_leave'),
    path('<slug:group_slug>/attendance',views.attendance_mark_view,name='group_attendance'),
    path('<slug>/delete',views.GroupDelete.as_view(),name='group_delete'),
    # path('group/<slug:group_slug>/attendance/<int:attendance_id>/update/', views.AttendanceUpdateView.as_view(), name='attendance_update'),
    path('<slug>/attendanceView',views.student_attendance_view,name='list_attendance')
]