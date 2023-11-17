from django import forms
from .models import Teacher
# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
# https://stackoverflow.com/questions/17873855/manager-isnt-available-user-has-been-swapped-for-pet-person/17874111#17874111

# to save password as hash value
# from django.contrib.auth.hashers import make_password
from django.http import HttpResponse

from django.contrib.auth.forms import UserCreationForm

# https://stackoverflow.com/questions/17873855/manager-isnt-available-user-has-been-swapped-for-pet-person/17874111#17874111
User = get_user_model()

class UserForm(UserCreationForm):
    class Meta():
        model = User
        fields = ['username','password1','password2']
        widgets = {
                'username': forms.TextInput(attrs={'class':'answer'}),
                'password1': forms.PasswordInput(attrs={'class':'answer'}),
                'password2': forms.PasswordInput(attrs={'class':'answer'}),
                }
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['username'].label = 'Enter Username'
        self.fields['password1'].label =  'Enter Password'
        self.fields['password2'].label = 'Re-Enter Password'


class TeacherCreateForm(forms.ModelForm):
    class Meta():
        model = Teacher
        fields = (
            'name',
            'email',
            'department',
            'whatsno',           
        )

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['name'].label = 'Full Name'
        self.fields['email'].label =  'Email Address'
        self.fields['department'].label = 'select your department'
        self.fields['whatsno'].label = 'your whatsapp no:'


    # def save(self, commit=True):
    #     user = super(TeacherCreateForm, self).save(commit=False)
    #     user.username = self.cleaned_data['user'].username
    #     user.set_password(self.cleaned_data['password'])
    #     if commit:
    #         user.save()
    #         self.save_m2m()
    #     return user    


class TeacherUpdateForm(forms.ModelForm):
    class Meta():
        model = Teacher
        fields = [
            'name',
            'email',
            'department',
            'whatsno',
        ]

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['name'].label = 'Full Name'
        self.fields['email'].label =  'Email Address'
        self.fields['department'].label = 'select your department'
        self.fields['whatsno'].label = 'your whatsapp no:'