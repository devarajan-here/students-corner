from django.shortcuts import render, reverse, get_object_or_404,redirect

# Create your views here.

from . import models
from django.views import generic,View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.utils import IntegrityError
from django.contrib import messages
from .forms import AttendanceForm
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy

class CreateGroup(generic.CreateView,LoginRequiredMixin):
    model = models.Group
    fields = (
            'name',
            'for_class',
            'class_start_date',
            )
    template_name = 'Groups/new.html'
    success_url = reverse_lazy('groups:group_list')

    def form_valid(self,form):
        # form.instance = self.request.user.is_teacher
        # response = super().form_valid(form)
        group = form.save()

        models.GroupMembers.objects.create(students=self.request.user,group=group)
        # return response

        return super().form_valid(form)

class GroupDetailView(generic.DetailView,LoginRequiredMixin):
        model = models.Group
        template_name = 'Groups/group_detail.html'


class GroupListView(generic.ListView,LoginRequiredMixin):
        model = models.Group
        template_name = 'Groups/group_list.html'        

class GrpJoin(generic.RedirectView,LoginRequiredMixin):
        # return detail view of grp after joining
        def get_redirect_url(self,*args,**kwargs):
                return reverse('groups:group_detail',kwargs={'slug':self.kwargs.get('slug')})

        def get(self, request,*args,**kwargs):
                group = get_object_or_404(models.Group,slug=self.kwargs.get('slug'))

                # need to add if user is teacher |  student

                try:
                    models.GroupMembers.objects.create(students=self.request.user,group=group)
                except IntegrityError:
                    messages.warning(self.request, 'Already a member')
                else:
                    messages.success(self.request, 'You are a Member')
                return super().get(request,*args,**kwargs)    
                        

class GrpLeave(LoginRequiredMixin,generic.RedirectView):
        def get_redirect_url(self,*args,**kwargs):
                return reverse('groups:group_detail',kwargs={'slug':self.kwargs.get('slug')})

        def get(self, request,*args,**kwargs):
                try:
                    membership = models.GroupMembers.objects.filter(
                        students=self.request.user,
                        group__slug=self.kwargs.get('slug')
                        ).get()
                
                except models.GroupMembers.DoesNotExist:
                        messages.warning(self.request,
                                 'No Members found to remove!'
                                 )
                       
                else:
                     membership.delete()
                     messages.success(self.request,
                                 'Sucessfully Left the group'
                                 )
                return super().get(request,*args,**kwargs)   

class GroupDelete(LoginRequiredMixin,generic.DeleteView):
        success_url = reverse_lazy('groups:group_list')
        model = models.Group



@login_required
def attendance_mark_view(request, group_slug):
    group = get_object_or_404(models.Group, slug=group_slug)

    if request.method == 'POST':
        form = AttendanceForm(request.POST, group=group)
        if form.is_valid():
            attendance = form.save(commit=False)
            attendance.group = group 
            attendance.save()
            form.save_m2m()  

            return redirect('groups:group_detail', slug=group_slug)
        else:
            print(form.errors)
            return HttpResponse(form.errors)
    else:
        form = AttendanceForm(group=group)
    
    return render(request, "Groups/attendance_create.html", {'create_attendanceform': form})

@login_required
def student_attendance_view(request, slug):
    group = get_object_or_404(models.Group, slug=slug)
    students = group.students.all()

    attendance_records = models.AttendanceStatus.objects.filter(attendance__group=group).select_related('student').order_by('attendance__date')

    context = {
        'students': students,
        'attendance_records': attendance_records
    }

    return render(request, 'Groups/group_attendance_list.html', context)



#     return render(request, 'Groups/group_attendance_list.html', context)
#     return render(request, "Groups/group_attendance_list.html", {'group': group, 'students': students, 'attendance_records': attendance_records})

#     group = get_object_or_404(models.Group, slug=slug)
#     students = models.Student.objects.all()

#     attendance_records = []
#     for student in students:
#         records = models.AttendanceStatus.objects.filter(attendance__group=group, student=student).order_by('attendance__date')
#         attendance_records.append((student, records))

#     sorted_attendance_records = sorted(attendance_records, key=lambda record: record.attendance.date)

#     context = {
#         'students': students,
#         'attendance_records': sorted_attendance_records
#     }
#     for n in attendance_records:
#         print(n)
#     return render(request, 'Groups/group_attendance_list.html', {'group':group,'attendance_records':attendance_records})



# class AttendanceUpdateView(LoginRequiredMixin,generic.UpdateView):
#     model = models.Attendence
#     form_class = AttendanceForm
#     template_name = 'Groups/attendance_update.html'
#     context_object_name = 'attendance'

#     def get_object(self, queryset=None):
#         group_slug = self.kwargs.get('group_slug')
#         attendance_id = self.kwargs.get('attendance_id')
#         return get_object_or_404(Attendance, group__slug=group_slug, id=attendance_id)

#     def get_success_url(self):
#         group_slug = self.kwargs.get('group_slug')
#         return reverse('groups:group_detail', kwargs={'slug': group_slug})

#     def form_valid(self, form):
#         attendance = form.save(commit=False)
#         absent_students = form.cleaned_data['absent_students']

#         # Update the AttendanceStatus for each student in the attendance
#         attendance_status_list = AttendanceStatus.objects.filter(attendance=attendance)
#         for attendance_status in attendance_status_list:
#             is_present = True
#             if absent_students and attendance_status.student.roll_no in absent_students:
#                 is_present = False
#             attendance_status.is_present = is_present
#             attendance_status.save()

#         return super().form_valid(form)

# <!-- <a class="btn btn-outline-success" href="{% url 'groups:attendance_update' group_slug=group.slug attendance_id=attendance.id %}">Update Attendance</a> -->