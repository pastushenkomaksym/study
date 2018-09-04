from django import forms
from .models import Student, Teacher, Clas


class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ('first_name', 'last_name', 'email', 'phone_number', 'subj')


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('first_name', 'last_name', 'email', 'phone_number', 'avg_mark', 'clas')


class ClasForm(forms.ModelForm):
    class Meta:
        model = Clas
        fields = ('name', 'teacher')
