from django.shortcuts import render,get_object_or_404,redirect

# Create your views here.
from django.views import generic
from .forms import TeacherCreateForm
from django.urls import reverse_lazy,reverse
from . import views,models,forms
from django.http import HttpResponse,HttpResponseRedirect

from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib.auth.decorators import login_required


def TeacherRegister(request):
    registed = False

    if request.method == 'POST':
        user_form = forms.UserForm(data=request.POST)
        teachercreate_form = forms.TeacherCreateForm(data=request.POST)

        if user_form and teachercreate_form.is_valid():
            user = user_form.save()
            # if user.password1 != user.password2:
            #     return HttpResponse('Password not Matching !!')
            # else:
            user.is_teacher = True
            user.save() #savd username & passwrd

            teacher = teachercreate_form.save(commit=False)
            teacher.user = user

            teacher.save()

            registed = True

        else:
            print(teachercreate_form.errors,user_form.errors)
            return HttpResponse(teachercreate_form.errors,user_form.errors)
    else:
        user_form = forms.UserForm()
        teachercreate_form = forms.TeacherCreateForm()

    return render(request, 'Teacher/signin.html',{'teacheruser_form':user_form,'teachercreate_form':teachercreate_form,'registed':registed})




def User_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('home'))

            else:
                HttpResponse('Account not Fount')
        
        else:
            print('User Login Faild')
            print(f""" 
            Tried Data
            username : {username}
            password : {password}
            """)

            return HttpResponse('Invalid details Provided')

    else:
        return render(request, 'login.html')


@login_required # without login no logout is req! Decorator
def User_logout(request):
    logout(request)
    print('Logout Sucess')
    return HttpResponseRedirect(reverse('home')) # change it later now testing




class TeacherDetail(generic.DetailView,LoginRequiredMixin):
    login_url = 'teacher/login/'
    model = models.Teacher
    fields = ('name','email','department','whatsno')
    template_name = 'Teacher/teacheraccount_detail.html'

@login_required
def TeacherUpdateView(request,pk):
    updated = False
    teacheracc = get_object_or_404(models.Teacher,pk=pk)
    if request.method == 'POST':
        update_form = forms.TeacherUpdateForm(data=request.POST,instance=teacheracc)
        if update_form.is_valid():
            update_form.save()
            return HttpResponseRedirect(reverse('home'))
        else:
            print(update_form.errors)
            return HttpResponse(update_form.errors)
    else:
        update_form = forms.TeacherUpdateForm(data=request.POST or None,instance=teacheracc)
    
    return render(request, 'Teacher/teacher_update.html',{'is_updated':updated,'update_form':update_form})

