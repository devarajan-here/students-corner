from django import forms
from .models import Student
from Teacher.forms import UserForm


class StudentCreateForm(forms.ModelForm):
    class Meta():
        model = Student
        fields = (
            'name',
            'email',
            'roll_no',
            'parrent_phno',
            'whatsno',
            'department',
        )

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['name'].label = 'Full Name'
        self.fields['email'].label =  'Email Address'
        self.fields['department'].label = 'select your department'
        self.fields['whatsno'].label = 'your whatsapp no:'
        self.fields['roll_no'].label = 'Roll no:'
        self.fields['parrent_phno'].label = 'Parrent Phone number'




