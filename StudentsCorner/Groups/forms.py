from django import forms
from .models import Group,Attendence,AttendanceStatus
from Student.models import Student


class AttendanceForm(forms.ModelForm):
    absent_students = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'Enter absent student roll numbers separated by comma'}))

    class Meta:
        model = Attendence
        fields = ['date']

    def __init__(self, *args, **kwargs):
        self.group = kwargs.pop('group')
        super().__init__(*args, **kwargs)
        self.fields['date'].widget.attrs['class'] = 'datepicker'

    def clean_absent_students(self):
        roll_numbers = self.cleaned_data['absent_students']
        if roll_numbers:
            roll_numbers = [roll.strip() for roll in roll_numbers.split(',')]
            print(roll_numbers)
        return roll_numbers

    def save(self, commit=True):
        attendance = super().save(commit=False)
        attendance.group = self.group
        if commit:
            attendance.save()

            absent_students = self.cleaned_data['absent_students']
            students = self.group.students.all()

            for student in students:
                is_present = True
                if absent_students and student.roll_no in absent_students:
                    is_present = False

                AttendanceStatus.objects.create(
                    attendance=attendance,
                    student=student,
                    is_present=is_present
                )

        return attendance



