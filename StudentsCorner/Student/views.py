from django.shortcuts import render
from Teacher.forms import UserForm
# Create your views here.
from . import forms
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from . import models

from django.contrib.auth.decorators import login_required

from django.http import HttpResponse

def StudentRegister(request):
    registed = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        studentcreate_form = forms.StudentCreateForm(data=request.POST)

        if user_form and studentcreate_form.is_valid():

            user = user_form.save()
            user.is_student = True
            user.save()

            student = studentcreate_form.save(commit=False)
            student.user = user

            if student.parrent_phno == student.whatsno:
                return HttpResponse("both can't be same | Give Proper parrent no/Whatsapp no ")
            

            student.save()

            registed = True

        else:
            print(user_form.errors,studentcreate_form.error_class)
            return HttpResponse(user_form.errors,studentcreate_form.error_class)
    else:
        user_form = UserForm()
        studentcreate_form = forms.StudentCreateForm()

    return render(request, 'Student/student_signup.html',{"Suser_form":user_form,'student_form':studentcreate_form,'registed':registed})
    

class StudetDetail(LoginRequiredMixin,generic.DeleteView):
    model = models.Student
    fields =  ['name','email','roll_no','department','whatsno','parrent_phno']
    template_name = 'Student/student_detail.html'

@login_required
def StudentUpdateView(request,pk):
    updated = False
    studacc = get_object_or_404(models.Student,pk=pk)
    if request.method == 'POST':
        update_form = forms.TeacherUpdateForm(data=request.POST,instance=studacc)
        if update_form.is_valid():
            update_form.save()
            return HttpResponseRedirect(reverse('home'))
        else:
            print(update_form.errors)
            return HttpResponse(update_form.errors)
    else:
        update_form = forms.TeacherUpdateForm(data=request.POST or None,instance=studacc)
    
    return render(request, 'Student/student_update.html',{'is_updated':updated,'update_form':update_form})

